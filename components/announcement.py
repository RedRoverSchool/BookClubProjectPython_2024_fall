import os
import allure
from playwright.sync_api import Page, expect
from core.settings import list_url


class Announcement:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Заполняем Ф.И.О")
    def fill_out_fullname(self):
        self.page.fill('input[name="name"]', "Jon Snow")

    @allure.step('Заполняем поле "Опишите себя"')
    def fill_out_descripption(self):
        self.page.fill("#id_description", "Great teacher")

    @allure.step("Загружаем фото")
    def upload_photo(self):
        root_dir = os.environ.get("ROOT_DIR")
        photo_path = os.path.join(
            root_dir, "Data", "upload_files", "stock-photo-handsome-cheerful-man.jfif"
        )
        photo_field = self.page.locator("#id_photo")
        photo_field.set_input_files(photo_path)
        # self.page.locator('input[name="photo"]').set_input_files(
        #     "Data/upload_files/stock-photo-handsome-cheerful-man.jfif"
        # )

    @allure.step("Выбираем категорию")
    def pick_category(self):
        dropdown = self.page.locator("#id_category")
        dropdown.select_option(value="1")
        selected_value = dropdown.input_value()
        assert selected_value == "1", "The category 'Математика' should be selected"

    @allure.step("Указываем опыт")
    def fill_out_experience(self):
        years_of_experience_input = self.page.locator("#id_years_of_experience")
        years_of_experience_input.fill("5")
        filled_value = years_of_experience_input.input_value()
        assert filled_value == "5", "The years of experience should be 5"

    @allure.step("Есть профильное образование")
    def checkbox_degree(self):
        degree_checkbox = self.page.locator("#id_has_degree")
        degree_checkbox.check()
        assert (
            degree_checkbox.is_checked()
        ), "The 'has degree' checkbox should be checked"

    @allure.step("Бесплатное первое занятие")
    def checkbox_free_first_lesson(self):
        free_first_lesson_checkbox = self.page.locator("#id_free_first_lesson")
        free_first_lesson_checkbox.check()
        assert (
            free_first_lesson_checkbox.is_checked()
        ), "The 'free first lesson' checkbox should be checked"

    @allure.step("Вводим стоимость занятия")
    def fill_out_price(self):
        price_input = self.page.locator("#id_price")
        price_input.fill("1000")
        filled_value = price_input.input_value()
        assert filled_value == "1000", "The price should be 1000"

    @allure.step("Длительность занятия")
    def fill_out_class_duration(self):
        class_duration_input = self.page.locator("#id_class_duration")
        class_duration_input.fill("60")
        filled_value = class_duration_input.input_value()
        assert filled_value == "60", "The class duration should be 60 minutes"

    @allure.step("Добавляем контактную информацию")
    def add_contact_info(self):
        contact_detail_input = self.page.locator("#id_phone")
        contact_detail_input.fill("5555555555")
        filled_value = contact_detail_input.input_value()
        assert filled_value == "5555555555", "Phone number should be 5555555555"

    @allure.step('Нажимаем на кнопку "Сохранить"')
    def click_save_announcement_btn(self):  # click_create_announcement_btn
        create_button = self.page.locator(
            '//button[@type="submit" and contains(@class, "btn-dark") and text()="Сохранить"]'
        )
        create_button.click()
        assert (
            self.page.url
            == "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
        )

    @allure.step("Пройти на страницу объявлений пользователя-учителя")
    def navigate_to_users_announcement_list(self):
        announcement_list_url = "http://testing.misleplav.ru/listings/my_listing/"
        self.page.goto(announcement_list_url)

    @allure.step("Убедиться, что количество объявлений пользователя-учителя равно нулю")
    def verify_number_of_announcements_is_zero(self):
        announcement_list = self.page.locator("main .container h5")
        expect(announcement_list).to_have_count(0)

    @allure.step("Убедиться, что пользователь на странице объявлений")
    def verify_announcements_page_endpoint(self):
        announcement_page_endpoint = "/listings/list/"
        current_url = self.page.url
        print(current_url)
        assert announcement_page_endpoint in current_url

    @allure.step("Кликаем на кнопку 'Мое объявление' в хедере")
    def click_my_announcement_button(self):
        self.page.locator("a", has_text="Мое объявление").click()
        expect(self.page).to_have_url(
            "http://testing.misleplav.ru/listings/my_listing/"
        )

    @allure.step("Кликаем на кнопку 'Сделать объявление видимым для учеников'")
    def click_make_announcement_invisible(self):
        self.page.get_by_role(
            "link", name="Сделать обьявление видимым для учеников"
        ).click()

    @allure.step(
        "Проверяем изменение текста кнопки на 'Сделать объявление невидимым для учеников'"
    )
    def check_button_text_invisible(self):
        expect(self.page.get_by_role("main")).to_contain_text(
            "Сделать обьявление невидимым для учеников"
        )

    @allure.step("Кликаем на кнопку 'Сделать объявление невидимым для учеников'")
    def click_make_announcement_visible(self):
        self.page.get_by_role(
            "link", name="Сделать обьявление невидимым для учеников"
        ).click()

    @allure.step(
        "Проверяем изменение текста кнопки на 'Сделать объявление невидимым для учеников'"
    )
    def check_button_text_visible(self):
        expect(self.page.get_by_role("main")).to_contain_text(
            "Сделать обьявление видимым для учеников"
        )

    @allure.step(
        "Проходим по всему списку обьявлений и проверяем, что карточки с именем учителя нет"
    )
    def check_teacher_announcement_invisible(self):
        self.page.get_by_role("link", name="Мое объявление").click()
        self.page.get_by_role("link", name="Редактировать").click()
        name_field = self.page.get_by_label("ФИО*")
        teacher_name = name_field.input_value()
        print("teacher_name", teacher_name)
        self.page.goto(list_url)

        current_page = 1
        teacher_found = False
        while True:
            allure.step(f"Проверяем страницу {current_page}")
            if self.page.get_by_text(teacher_name, exact=True).count() > 0:
                teacher_found = True
                break

            next_button = self.page.get_by_role("link", name="Вперед").first
            if not next_button.is_visible():
                break

            self.page.get_by_role("link", name="Вперед").click()
            self.page.wait_for_load_state("networkidle")
            current_page += 1

        assert not teacher_found, f"Объявление с именем '{teacher_name}' найдено!"

    @allure.step("Убедиться что имя в объявлении совпадает с заданным")
    def verify_announcement_tutor_name(self, expected_name):
        tutor_name_announcement = self.page.locator("h5").inner_text()
        assert expected_name == tutor_name_announcement

    @allure.step("Убедиться, что обязательные поля не заполнены")
    def verify_required_fields_are_not_filled(self):
        error_message = self.page.locator(
            '//strong[text()="Обязательное поле."]'
        ).count()
        assert error_message == 8

    @allure.step("Создаем объявление")
    def create_announcement(self):
        self.fill_out_fullname()
        self.fill_out_descripption()
        self.upload_photo()
        self.pick_category()
        self.fill_out_experience()
        self.checkbox_degree()
        self.fill_out_price()
        self.fill_out_class_duration()
        self.checkbox_free_first_lesson()
        self.add_contact_info()
        self.click_save_announcement_btn()

    @allure.step("Создаем объявление с обязательными полями")
    def create_announcement_with_only_required_fields(self):
        self.fill_out_fullname()
        self.fill_out_descripption()
        self.upload_photo()
        self.pick_category()
        self.fill_out_experience()
        self.fill_out_price()
        self.fill_out_class_duration()
        self.add_contact_info()
        self.click_save_announcement_btn()

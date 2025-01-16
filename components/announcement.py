import os
import allure
from playwright.sync_api import Page, expect
from core.settings import list_url
from core.settings import edit_announcement_url
import re


class Announcement:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Заполняем 'Ваше имя'")
    def fill_first_name(self):
        self.page.fill('input[name="first_name"]', "Thomas")

    @allure.step("Заполняем 'Ваша фамилия'")
    def fill_last_name(self):
        self.page.fill('input[name="last_name"]', "Peters")

    @allure.step("Заполняем 'Telegram'")
    def fill_telegram(self):
        self.page.fill('input[name="telegram"]', "ThomasP")

    @allure.step("Заполняем 'Телефон'")
    def fill_phone_number(self):
        self.page.fill('input[name="phone"]', "14103902623")

    @allure.step('Заполняем поле "Опишите себя"')
    def fill_out_descripption(self):
        self.page.fill("#id_description", "Great teacher")

    @allure.step("Загружаем фото")
    def upload_photo(self):
        try:
            root_dir = os.environ.get("ROOT_DIR")
            photo_path = os.path.join(
                root_dir,
                "Data",
                "upload_files",
                "stock-photo-handsome-cheerful-man.jfif",
            )
            photo_field = self.page.locator("#id_photo")
            photo_field.set_input_files(photo_path)
        except Exception as e:
            print(f"First upload error: {e}")
            try:
                self.page.locator('input[name="photo"]').set_input_files(
                    "Data/upload_files/stock-photo-handsome-cheerful-man.jfif"
                )
            except Exception as e:
                print(f"Second upload failed with error: {e}")

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

    @allure.step("Вводим стоимость занятия")
    def fill_out_price(self):
        price_input = self.page.locator("#id_price")
        price_input.fill("1000")
        filled_value = price_input.input_value()
        assert filled_value == "1000", "The price should be 1000"

    @allure.step("Продолжительность занятия")
    def fill_out_class_duration(self):
        class_duration_input = self.page.locator('input[name="class_duration"]')
        class_duration_input.fill("60")
        filled_value = class_duration_input.input_value()
        assert filled_value == "60", "The class duration should be 60 minutes"

    @allure.step("Продавать пакеты со скидкой")
    def checkbox_discount(self):
        discount_checkbox = self.page.locator("#id_package_discounts")
        discount_checkbox.check()
        assert (
            discount_checkbox.is_checked()
        ), "The 'has degree' checkbox should be checked"

    @allure.step('Заполняем поле "Удобное время для занятий"')
    def fill_out_convenient_time(self):
        self.page.fill(
            "#id_convenient_time_slots",
            "Понедельник-Пятница с 10.00-11.00 " "Суббота и Воскресенье выходные",
        )

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

    @allure.step("Кликаем кнопку 'Редактировать объявление'")
    def click_edit_announcement_button(self):
        self.page.locator("a", has_text="Редактировать").click()

    @allure.step("Кликаем кнопку 'Просмотреть объявление'")
    def click_view_announcement_button(self):
        self.page.locator("a", has_text="Просмотреть").click()

    @allure.step("Проверяем URL страницы объявления по шаблону")
    def check_announcement_url_by_template(self):
        current_url = self.page.url
        pattern = r"^http://tester:dslfjsdfblkhew%40122b1klbfw@testing\.misleplav\.ru/listings/\d+/$"
        assert re.match(
            pattern, current_url
        ), f"URL не соответствует ожидаемому шаблону: {current_url}"

    @allure.step("Проверяем URL страницы редактирования объявления")
    def check_edit_announcement_page_url(self):
        expect(self.page).to_have_url(edit_announcement_url)

    @allure.step("Проверяем видимость счетчика просмотров")
    def check_view_counter_visible(self):
        expect(self.page.locator("p.mt-4.text-center.text-secondary")).to_be_visible()

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
        error_message_count = self.page.locator(
            '//strong[text()="Обязательное поле."]'
        ).count()
        print(f"Found {error_message_count} error messages.")
        assert (
            error_message_count == 8
        ), f"Expected 8 error messages, but found {error_message_count}"

    @allure.step("Создаем объявление")
    def create_announcement(self):
        self.fill_first_name()
        self.fill_last_name()
        self.fill_telegram()
        self.fill_phone_number()
        self.fill_out_descripption()
        self.upload_photo()
        self.pick_category()
        self.fill_out_experience()
        self.checkbox_degree()
        self.fill_out_price()
        self.fill_out_class_duration()
        self.checkbox_discount()
        self.fill_out_convenient_time()
        self.click_save_announcement_btn()

    @allure.step("Создаем объявление с обязательными полями")
    def create_announcement_with_only_required_fields(self):
        self.fill_first_name()
        self.fill_last_name()
        self.fill_telegram()
        self.fill_phone_number()
        self.fill_out_descripption()
        self.upload_photo()
        self.pick_category()
        self.fill_out_experience()
        self.fill_out_price()
        self.fill_out_class_duration()
        self.fill_out_convenient_time()
        self.click_save_announcement_btn()

    @allure.step("Проверяем, что все обязательные поля отмечены '*'/ 'Обязательное поле'")
    def mandatory_fields_are_marked_check(self):
        fields_to_check = [
            ("//label[@for='id_first_name']//span[@class='asteriskField']", "id_first_name"),
            ("//label[@for='id_last_name']//span[@class='asteriskField']", "id_last_name"),
            ("//label[@for='id_telegram']//span[@class='asteriskField']", "id_telegram"),
            ("//label[@for='id_phone']//span[@class='asteriskField']", "id_phone"),
            ("//label[@for='id_description']//span[@class='asteriskField']", "id_description"),
            ("//legend[@class='form-label requiredField']//span[@class='asteriskField']", "student_category"),
            ("//label[@for='id_can_help']//span[@class='asteriskField']", "id_can_help"),
            ("//label[@for='id_category']//span[@class='asteriskField']", "id_category"),
            ("//label[@for='id_years_of_experience']//span[@class='asteriskField']", "id_years_of_experience"),
            ("//label[@for='id_price']//span[@class='asteriskField']", "id_price"),
            ("//label[@for='id_class_duration']//span[@class='asteriskField']", "id_class_duration"),
        ]

        for locator, field_name in fields_to_check:
            field_mark = self.page.locator(locator)
            assert field_mark.is_visible(), f"Отметка поля с локатором {field_name} не найдена"

        download_photo_title_text = self.page.get_by_text("Рекомендуемое разрешение:").inner_text()
        assert "Обязательное поле." in download_photo_title_text, (
            f"Текст 'Обязательное поле.' не найден в {download_photo_title_text}"
        )



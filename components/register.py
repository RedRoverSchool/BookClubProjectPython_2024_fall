import allure
from playwright.sync_api import Page, expect


class Register:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем заголовок 'Регистрация'")
    def header_should_contain_text(self, title_text):
        expect(self.page.get_by_test_id("registration-header")).to_contain_text(
            title_text
        )

    @allure.step("Заполняем поле 'Придумайте ник'")
    def fill_nick(self, nick):
        self.page.get_by_placeholder("Придумайте ник").fill(nick)

    @allure.step("Заполняем поле 'Придумайте пароль'")
    def fill_password(self, password):
        self.page.get_by_placeholder("Придумайте пароль").fill(password)

    @allure.step("Заполняем поле 'Подтвердите пароль'")
    def fill_confirm_password(self, password):
        self.page.get_by_placeholder("Подтвердите пароль").fill(password)

    @allure.step("Кликаем на кнопку 'Я преподаватель'")
    def click_on_become_a_teacher_button(self):
        self.page.locator("#id_is_tutor").check()

    @allure.step("Кликаем на кнопку 'Зарегистрироваться'")
    def click_on_registration_button(self):
        self.page.get_by_test_id("submit-button").click()

    @allure.step("Проверяем, что страница регистрации открыта")
    def verify_registration_page_opened(self):
        registration_title = self.page.locator("h1").inner_text()
        assert (
            registration_title == "Регистрация"
        ), f"Ожидался заголовок 'Регистрация', но найдено: {registration_title}"

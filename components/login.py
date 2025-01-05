import allure
from playwright.sync_api import Page
from core.settings import login_url


class Login:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем URL страницы 'Логин'")
    def check_url_login_page(self, expected_part: str):
        current_url = self.page.url
        assert (
            expected_part in current_url
        ), f"Ожидалось, что '{expected_part}' будет частью '{current_url}'"

    @allure.step("Проверяем наличие кнопки 'Регистрация'")
    def check_title_of_registration(self):
        title = self.page.get_by_title("Регистрация")
        assert "Регистрация", title

    def open_login_page(self):
        self.page.goto(login_url)

    @allure.step("Проверяем видимость поля ввода логина")
    def login_field_should_be_visible(self):
        field = self.page.locator("#id_username")
        assert field.is_visible()

    @allure.step("Проверяем видимость поля ввода пароля")
    def password_field_should_be_visible(self):
        field = self.page.locator("#id_password")
        assert field.is_visible()

    @allure.step("Проверяем видимость кнопки 'Войти'")
    def login_dark_button_should_be_visible(self):
        button = self.page.locator('button[type="submit"]')
        assert button.is_visible()

    @allure.step("Проверяем видимость сообщения о не правильном вводе логина и пароля")
    def invalid_credentials_message_should_be_visible(self):
        text = "Пожалуйста, введите правильные email и пароль. Оба поля могут быть чувствительны к регистру."
        message = self.page.locator(f"ul li:has-text('{text}')")
        assert message.is_visible()

    @allure.step("Проверяем видимость текста 'Нет аккаунта'")
    def login_text_should_be_visible(self):
        text = self.page.locator(".text-center.mt-3")
        assert text.is_visible()

    @allure.step("Проверяем видимость активного URL 'Создать учетную запись'")
    def login_active_url_should_be_visible(self):
        active_url = self.page.locator("a.text-dark")
        assert active_url.is_visible()

    @allure.step("Нажимаем 'Создать учетную запись' URL")
    def click_create_account_url(self):
        create_account_url = self.page.locator(".text-dark")
        create_account_url.click()

    @allure.step("Вводим логин пользователя")
    def enter_username(self, username: str):
        username_field = self.page.locator("#id_username")
        username_field.fill(username)

    @allure.step("Вводим пароль пользователя")
    def enter_password(self, password: str):
        password_field = self.page.locator("#id_password")
        password_field.fill(password)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login_button(self):
        self.page.get_by_text("Войти").click()

    @allure.step("Выполняем полный вход пользователя")
    def full_login(self, username: str, password: str):
        """
        Выполняет полный процесс входа на сайт.
        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        """
        self.click_login_button()
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()

    @allure.step("Выполняем вход с не корректным логином")
    def check_enter_invalid_username(self, username):
        self.enter_username(username)

    def should_be_valid_message(self, expected_text):
        expected_messege_field = self.page.locator(
            "//*[contains(text(), 'Пожалуйста,')]"
        )
        actual_text = expected_messege_field.text_content()
        assert (
            expected_messege_field.is_visible()
        ), "Сообщение с текстом 'Пожалуйста' не найдено"
        assert expected_text == actual_text

    def click_submit_button(self):
        self.page.locator("//*[@type='submit']").click()

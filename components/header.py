import allure
from playwright.sync_api import Page, expect

from core.settings import base_url


class Header:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем Хэдер на главной странице")
    def visit(self):
        self.page.goto(base_url)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_on_login_button(self):
        self.page.locator(
            '(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]'
        ).click()

    @allure.step("Кликаем на кнопку 'Регистрация'")
    def click_on_registration_button(self):
        self.page.get_by_test_id("signup").click()

    @allure.step("Проверяем видимость кнопки 'Создать объявление'")
    def create_listing_button_should_be_visible(self):
        expect(self.page.get_by_test_id("create-listing")).to_be_visible()

    @allure.step("Кликаем на кнопку 'Найти репетитора'")
    def click_on_find_tutor_button(self):
        self.page.locator("//li/a[text() = 'Найти репетитора']").click()

    @allure.step("Проверяем видимость кнопки 'Поддержка'")
    def support_button_should_be_visible(self):
        button = self.page.locator(
            "//a[contains(@class, 'btn') and text()='Поддержка']"
        )
        expect(button).to_be_visible()

    @allure.step("Кликаем на кнопку 'Поддержка'")
    def click_on_support_button(self):
        button = self.page.locator(
            "//a[contains(@class, 'btn') and text()='Поддержка']"
        )
        button.click()
        expect(self.page).to_have_url("https://t.me/misleplav_support_bot")

    @allure.step("Наводим мышку на кнопку 'Поддержка' и проверяем изменение цвета")
    def hover_support_button_color_check(self):
        button = self.page.locator(
            "//a[contains(@class, 'btn') and text()='Поддержка']"
        )
        original_color = button.evaluate(
            "el => window.getComputedStyle(el).backgroundColor"
        )
        button.hover()
        expect(button).not_to_have_css("background-color", original_color)

    @allure.step("Проверяем видимость кнопки 'Профиль'")
    def profile_button_should_be_visible(self):
        button = self.page.locator("[data-testid='profile']")
        expect(button).to_be_visible()

    @allure.step("Кликаем на кнопку 'Профиль'")
    def click_on_profile_button(self):
        button = self.page.get_by_test_id("profile")
        button.click()
        expect(self.page).to_have_url("http://testing.misleplav.ru/profile/")

    @allure.step("Проверяем видимость кнопки 'Войти'")
    def login_button_should_be_visible(self):
        button = self.page.locator(
            '(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]'
        )
        assert button.is_visible()

    @allure.step("Проверяем видимость кнопки 'Стать репетитором'")
    def become_a_tutor_button_should_be_visible(self):
        button = self.page.locator(
            '//a[@class="btn btn-light rounded d-none d-sm-inline btn-lg"]'
        )
        assert button.is_visible()

    @allure.step("Проверяем доступна ли кнопка 'Войти' для взаимодействия")
    def login_button_is_enabled(self):
        button = self.page.locator('//*[@id="navbarNav"]/ul/li[1]/a')
        assert button.is_enabled()

    @allure.step("Наводим мышку на кнопку 'Создать объявление' и проверяем изменение цвета")
    def hover_create_listing_btn(self):
        button = self.page.get_by_test_id("create-listing")
        base_color = button.evaluate('el => getComputedStyle(el).backgroundColor')
        button.hover()
        changed_color = button.evaluate('el => getComputedStyle(el).backgroundColor')
        return base_color,changed_color
import os

import allure
import pytest
import requests
from faker import Faker
from pytest import Item
from requests.auth import HTTPBasicAuth

from Data.constants import BASE_URL
from Data.constants import AUTH_CREDENTIALS
from components.announcement import Announcement
from components.find_tutor import FindTutor
from components.header import Header
from components.my_teachers import MyTeachersPage

from components.login import Login
from components.homepage import Homepage
from playwright.sync_api import Page, sync_playwright
from components.footer import Footer
from components.register import Register
from components.telegram_page import TelegramPage
from components.user_profile import UserProfile
from components.cookie_banner import CookieBanner
from components.create_announcement import CreateAnnouncement


@pytest.fixture
def header(page: Page):
    return Header(page)


@pytest.fixture
def my_teachers(page: Page):
    return MyTeachersPage(page)


@pytest.fixture
def register(page: Page):
    return Register(page)


@pytest.fixture
def homepage(page: Page):
    return Homepage(page)


@pytest.fixture
def login(page: Page):
    return Login(page)


@pytest.fixture
def find_tutor(page: Page):
    return FindTutor(page)


@pytest.fixture
def footer(page: Page):
    return Footer(page)


@pytest.fixture
def telegram_page(page: Page):
    return TelegramPage(page)


@pytest.fixture
def user_profile(page: Page):
    return UserProfile(page)


@pytest.fixture(scope="function", autouse=True)
def video_and_screenshot(page: Page):
    yield  # здесь выполняется тест

    # Сохранить скриншот
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    # Сохранить видео
    video = page.video.path()
    page.context.close()  # Закрыть контекст, чтобы видео сохранилось на диск
    allure.attach.file(
        video,
        name="video",
        attachment_type=allure.attachment_type.WEBM,
    )


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_call(item: Item):
    yield
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).title())


@pytest.fixture
def browser_context():
    with sync_playwright() as p:
        # Запускаем Chromium
        browser = p.chromium.launch(
            headless=os.environ.get(
                "CI_RUN", False
            ),  # Запуск в headless режиме, если это CI/CD
            args=[
                "--start-maximized",  # Максимизация окна
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ]
            if os.environ.get("CI_RUN")
            else [],
        )
        context = (
            browser.new_context()
        )  # Создаем контекст браузера без изменения размера окна
        yield context
        context.close()
        browser.close()


@pytest.fixture(autouse=True)
def set_root_dir():
    ci_root_dir = os.environ.get('GITHUB_WORKSPACE', False)
    os.environ['ROOT_DIR'] = ci_root_dir or '..'


@pytest.fixture
def cookie_banner(page: Page):
    return CookieBanner(page)


@pytest.fixture
def announcement(page: Page):
    return Announcement(page)


@pytest.fixture
def create_announcement_page(page: Page):
    return CreateAnnouncement(page)


@pytest.fixture(scope="function")
def fake_data():
    fake = Faker()
    data = {
        "email": fake.email(),
        "name": fake.name(),
        "password": fake.password(),
    }
    return data


@pytest.fixture(scope="function")
def create_user(fake_data, header, register):
    # Выполняем регистрацию
    header.visit()
    header.click_registration_button()
    user_data = register.complete_registration(fake_data)

    # Печатаем email и пароль из возвращаемого user_data
    print(f"Email: {user_data['email']}")
    print(f"Password: {user_data['password']}")
    return user_data


@pytest.fixture(scope="function")
def api_fake_data():
    fake = Faker()
    data = {
        "first_name": fake.name(),
        "email": fake.email(),
        "password": fake.password(),
        "is_tutor": True,
        "is_premium": True,
        "is_standart": True,
        "is_writer": True,
        "end_subscription": "2034-12-20",
    }
    return data


@pytest.fixture(scope="function")
def api_create_user(api_fake_data):
    response = requests.post(
        f'{BASE_URL}/api/users/',
        json=api_fake_data,
        auth=HTTPBasicAuth(*AUTH_CREDENTIALS)
    )

    if response.status_code == 201:
        created_user = response.json()
        return {
            "email": created_user['email'],
            "password": api_fake_data['password'],
            "user_data": created_user
        }
    else:
        print(f"Ошибка при создании пользователя: {response.status_code}")
        print(f"Ответ сервера: {response.text}")
        return None

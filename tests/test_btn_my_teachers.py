import pytest
from playwright.sync_api import Page

from components.my_teachers import MyTeachersPage


# AT_32.001.001.001 | Student > My teachers> Viewing My Teachers List > Navigate to the "My Teachers" Page


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_my_teachers_btn_exists(header, register, page: Page):
    """Проверка наличия кнопки 'Мои репетиторы'."""
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.check_my_teachers_btn_exists()


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_my_teachers_btn_click(header, register, page: Page):
    """Проверка клика на кнопку 'Мои репетиторы'."""
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.click_my_teachers_btn()
    my_teachers_button.verify_page_my_teachers_opened()


@pytest.mark.skip(reason="не прошёл CI после изменений 26.12.2024")
def test_check_teachers_list(header, register, page: Page):
    """Проверка что открылась страница 'Мои репетиторы' со списком репетиторов или без с соответствующим сообщением."""
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.click_my_teachers_btn()
    my_teachers_button.check_teachers_list()

from playwright.sync_api import Page

from components.my_teachers import MyTeachersPage


# AT_32.001.001.001 | Student > My teachers> Viewing My Teachers List > Navigate to the "My Teachers" Page
def test_my_teachers_btn_exists(header, login, page: Page):
    """Проверка наличия кнопки 'Мои репетиторы'."""
    header.visit()
    login.full_login("student849727@gmail.com", "xaD1n0tUfaHN")
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.check_my_teachers_btn_exists()


def test_my_teachers_btn_click(header, login, page: Page):
    """Проверка клика на кнопку 'Мои репетиторы'."""
    header.visit()
    login.full_login("student849727@gmail.com", "xaD1n0tUfaHN")
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.click_my_teachers_btn()
    my_teachers_button.verify_page_my_teachers_opened()


def test_check_teachers_list(header, login, page: Page):
    """Проверка что открылась страница 'Мои репетиторы' со списком репетиторов или без с соответствующим сообщением."""
    header.visit()
    login.full_login("student849727@gmail.com", "xaD1n0tUfaHN")
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.click_my_teachers_btn()
    my_teachers_button.check_teachers_list()

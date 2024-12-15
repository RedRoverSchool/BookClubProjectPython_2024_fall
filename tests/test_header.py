import pytest


def test_login_button_opens_login_page(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_url_login_page("/login")


def test_verify_registration_options_on_registration_page(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")


def test_verify_registration_options_on_login_page(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_title_of_registration()


def test_verify_registration_options_on_find_tutor_page(homepage, find_tutor):
    homepage.visit()
    homepage.click_on_find_tutor_button()
    find_tutor.select_category()
    find_tutor.free_first_lesson()
    find_tutor.filter()
    find_tutor.list_of_card_teacher()

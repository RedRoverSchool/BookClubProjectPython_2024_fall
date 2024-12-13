from faker import Faker

# from pydantic_settings import BaseSettings, SettingsConfigDict

fake = Faker()

base_url = "http://tester:dslfjsdfblkhew@122b1klbfw@testing.misleplav.ru"
fake_name_for_registration = fake.user_name()

policy_url = "https://www.example.com/privacy-policy"
list_url = (
    "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
)
signup_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/signup/"
login_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/login/"
title = "Example Domain"

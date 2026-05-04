import json
import time

import pytest

from uiTesting.pages.login_page import LoginPage
from uiTesting.pages.signup_page import SignUpPage


@pytest.mark.usefixtures("driver")
class TestLogin:
    with open("uiTesting/data/signup/happy_scenarios.json") as f :
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.login
    def test_login_happy_scenarios(self,driver,data):
        lg = LoginPage(driver)
        lg.login(data["email"],data["password"])
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestApartmentSystem\\uiTesting\\screenshots\\login\\happyscenarios\\{data['screenshot']}.png")

    with open("uiTesting/data/login/negative_scenarios.json") as f :
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.login
    def test_login_happy_scenarios(self,driver,data):
        lg = LoginPage(driver)
        lg.login(data["email"], data["password"])
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestApartmentSystem\\uiTesting\\screenshots\\login\\negativescenarios\\{data['screenshot']}.png")

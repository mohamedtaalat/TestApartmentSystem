import json
import time

import pytest

from uiTesting.pages.signup_page import SignUpPage


@pytest.mark.usefixtures("driver")
class TestSignup:
    with open("uiTesting/data/signup/happy_scenarios.json") as f :
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.signup
    def test_signup_happy_scenarios(self,driver,data):
        sg = SignUpPage(driver)
        time.sleep(2)
        sg.sign_up(data["name"],data["email"],data["password"],data["confirmPassword"],data["role"])
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestApartmentSystem\\uiTesting\\screenshots\\signup\\happyscenarios\\{data['screenshot']}.png")

    with open("uiTesting/data/signup/negative_scenarios.json") as f :
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.signup
    def test_signup_happy_scenarios(self,driver,data):
        sg = SignUpPage(driver)
        time.sleep(2)
        sg.sign_up(data["name"],data["email"],data["password"],data["confirmPassword"],data["role"])
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestApartmentSystem\\uiTesting\\screenshots\\signup\\negativescenarios\\{data['screenshot']}.png")

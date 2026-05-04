from selenium.webdriver.common.by import By

from uiTesting.base.basis import Base
class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email(self, email):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='email']"
        ).send_keys(email)

    def enter_password(self, password):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='password']"
        ).send_keys(password)

    def click_login(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def login(self, email, password):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[normalize-space()='Login']"
        ).click()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def click_signup(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[normalize-space()='Sign up for free']"
        ).click()


from selenium.webdriver.common.by import By

from uiTesting.base.basis import Base
class SignUpPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_name(self,name):
       self.wait_until_element_be_visible(
           By.XPATH
           , "//input[@id='name']"
       ).send_keys(name)

    def enter_email(self,email):
        self.wait_until_element_be_visible(
            By.XPATH
            , "//input[@id='email']"
        ).send_keys(email)

    def enter_password(self,password):
        self.wait_until_element_be_visible(
            By.XPATH
            , "//input[@id='password']"
        ).send_keys(password)

    def enter_confirm_password(self,password):
        self.wait_until_element_be_visible(
            By.XPATH
            , "//input[@id='confirmPassword']"
        ).send_keys(password)

    def select_role(self,role):
        if role == "tenant":
            self.wait_until_element_be_visible(
                By.XPATH,
                "//div[@class='_roleSelector_dfb1y_107']//button[1]"
            ).click()

        elif role == "owner":
            self.wait_until_element_be_visible(
                By.XPATH,
                "//button[2]"
            ).click()

    def click_sign_up(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def click_login(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[normalize-space()='Log in']"
        ).click()

    def sign_up(self,name,email,password,confirmPassword,role):
        self.wait_until_element_be_clickable(
            By.XPATH
            , "//a[normalize-space()='Register']"
        ).click()
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirmPassword)
        self.select_role(role)
        self.click_sign_up()
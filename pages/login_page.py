from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_TEXT = (By.XPATH, "//h6[text()='Dashboard']")
    ERROR_MESSAGE = (
        By.XPATH,
        "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']",
    )

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_dashboard_visible(self):
        return self.is_element_present(self.DASHBOARD_TEXT)

    def is_error_message_visible(self):
        return self.is_element_present(self.ERROR_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

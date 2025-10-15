from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    URL = "http://localhost:8000/contact_local.html"

    EMAIL = (By.ID, "email")
    NAME = (By.ID, "name")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit")
    SUCCESS = (By.ID, "success")
    ERROR = (By.ID, "error")

    def open_page(self):
        self.open(self.URL)

    def fill_form(self, email, name, message):
        self.type(self.EMAIL, email)
        self.type(self.NAME, name)
        self.type(self.MESSAGE, message)

    def submit_form(self):
        self.click(self.SUBMIT)

    def get_success_message(self):
        return self.get_text(self.SUCCESS)

    def get_error_message(self):
        return self.get_text(self.ERROR)

    def open_fill_submit_form(page, email, name, message):
        page.open_page()
        page.fill_form(email, name, message)
        page.submit_form()

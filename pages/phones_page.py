from selenium.webdriver.common.by import By
from .base_page import BasePage

class PhonesPage(BasePage):
    IPHONE_LINK = (By.XPATH, "//a[normalize-space()='iPhone']")

    def select_iphone(self):
        self.click(*self.IPHONE_LINK)
        self.wait(3)
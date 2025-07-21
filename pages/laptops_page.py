from selenium.webdriver.common.by import By
from .base_page import BasePage

class LaptopsPage(BasePage):
    SHOW_ALL_LAPTOPS = (By.XPATH, "//a[text()='Show AllLaptops & Notebooks']")
    HP_LINK = (By.XPATH, "//a[text()='HP LP3065']")

    def click_show_all(self):
        self.click(*self.SHOW_ALL_LAPTOPS)
        self.wait(2)

    def select_hp_laptop(self):
        self.click(*self.HP_LINK)
        self.wait(2)

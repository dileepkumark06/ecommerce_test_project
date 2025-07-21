from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from .base_page import BasePage

class HomePage(BasePage):
    PHONES_LINK = (By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(),'Phones & PDAs')]")
    LAPTOPS_LINK = (By.XPATH, "//a[text()='Laptops & Notebooks']")

    def goto_phones(self):
        self.click(*self.PHONES_LINK)

    def hover_laptops(self):
        laptop = self.find(*self.LAPTOPS_LINK)
        action = ActionChains(self.driver)
        action.move_to_element(laptop).perform()
        self.wait(2)

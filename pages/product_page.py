from selenium.webdriver.common.by import By
from .base_page import BasePage
import random

class ProductPage(BasePage):
    FIRST_THUMBNAIL = (By.XPATH, "//ul[@class='thumbnails']/li[1]")
    NEXT_BUTTON = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    CLOSE_BUTTON = (By.XPATH, "//button[@title='Close (Esc)']")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    CALENDAR_ICON = (By.XPATH, "//i[@class='fa fa-calendar']")
    CALENDAR_NEXT = (By.XPATH, "//th[@class='next']")
    MONTH_YEAR = (By.XPATH, "//th[@class='picker-switch']")
    CALENDAR_DATE_31 = (By.XPATH, "//td[text()='31']")

    def open_image_gallery(self):
        self.click(*self.FIRST_THUMBNAIL)
        self.wait(2)

    def click_next_image(self, times=5):
        next_button = self.find(*self.NEXT_BUTTON)
        for i in range(times):
            next_button.click()
            self.wait(3)

    def take_screenshot(self):
        filename = f'screenshot#{random.randint(0, 101)}.png'
        self.driver.save_screenshot(filename)
        self.wait(2)
        return filename

    def close_gallery(self):
        self.click(*self.CLOSE_BUTTON)
        self.wait(2)

    def set_quantity(self, qty):
        quantity_field = self.find(*self.QUANTITY_INPUT)
        quantity_field.click()
        self.wait(2)
        quantity_field.clear()
        self.wait(1)
        quantity_field.send_keys(str(qty))
        self.wait(1)

    def add_to_cart(self):
        add_cart_btn = self.find(*self.ADD_TO_CART_BUTTON)
        self.scroll_into_view(add_cart_btn)
        self.wait(2)
        add_cart_btn.click()
        self.wait(2)

    def set_calendar_date(self, target_month_year="December 2022"):
        calendar = self.find(*self.CALENDAR_ICON)
        calendar.click()
        
        next_click_calendar = self.find(*self.CALENDAR_NEXT)
        month_year = self.find(*self.MONTH_YEAR)
        
        while month_year.text != target_month_year:
            next_click_calendar.click()
            month_year = self.find(*self.MONTH_YEAR)
        
        self.click(*self.CALENDAR_DATE_31)
        self.wait(1)

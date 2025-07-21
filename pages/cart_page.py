from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_TOTAL = (By.ID, "cart-total")
    CHECKOUT_LINK = (By.XPATH, "//p[@class='text-right']/a[2]")

    def open_cart(self):
        self.click(*self.CART_TOTAL)
        self.wait(2)

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_LINK)
        self.wait(2)

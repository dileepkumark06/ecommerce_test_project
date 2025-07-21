from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class CheckoutPage(BasePage):
    GUEST_RADIO = (By.XPATH, "//input[@value='guest']")
    ACCOUNT_CONTINUE = (By.ID, "button-account")
    STEP_2_BILLING = (By.XPATH, "//a[text()='Step 2: Billing Details ']")
    
    # Billing form fields
    FIRSTNAME = (By.ID, 'input-payment-firstname')
    LASTNAME = (By.ID, 'input-payment-lastname')
    EMAIL = (By.ID, 'input-payment-email')
    TELEPHONE = (By.ID, 'input-payment-telephone')
    ADDRESS = (By.ID, 'input-payment-address-1')
    CITY = (By.ID, 'input-payment-city')
    POSTCODE = (By.ID, 'input-payment-postcode')
    COUNTRY = (By.ID, 'input-payment-country')
    REGION = (By.ID, 'input-payment-zone')
    
    # Continue buttons
    BILLING_CONTINUE = (By.XPATH, '//input[@id="button-guest"]')
    SHIPPING_CONTINUE = (By.XPATH, '//input[@id="button-shipping-method"]')
    TERMS_CHECKBOX = (By.XPATH, '//input[@name="agree"]')
    PAYMENT_CONTINUE = (By.XPATH, '//input[@id="button-payment-method"]')
    
    # Final order
    FINAL_PRICE = (By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
    CONFIRM_BUTTON = (By.ID, 'button-confirm')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="col-sm-12"]/h1')

    def select_guest_checkout(self):
        self.click(*self.GUEST_RADIO)
        self.click(*self.ACCOUNT_CONTINUE)
        self.wait(1)

    def scroll_to_billing_details(self):
        step_2 = self.find(*self.STEP_2_BILLING)
        self.scroll_into_view(step_2)
        self.wait(1)

    def fill_billing_details(self):
        self.enter_text(*self.FIRSTNAME, 'test_first_name')
        self.enter_text(*self.LASTNAME, 'test_last_name')
        self.enter_text(*self.EMAIL, 'test@test.com')
        self.enter_text(*self.TELEPHONE, '012345678')
        self.enter_text(*self.ADDRESS, 'teststreet 87')
        self.enter_text(*self.CITY, 'Bengaluru')
        self.enter_text(*self.POSTCODE, '560098')
        self.wait(3)

    def select_country_and_region(self):
        country_dropdown = Select(self.find(*self.COUNTRY))
        self.wait(2)
        country_dropdown.select_by_visible_text('India')
        self.wait(2)
        
        region_dropdown = Select(self.find(*self.REGION))
        self.wait(2)
        region_dropdown.select_by_visible_text('Karnataka')
        self.wait(2)

    def continue_billing(self):
        self.click(*self.BILLING_CONTINUE)
        self.wait(1)

    def continue_shipping(self):
        self.click(*self.SHIPPING_CONTINUE)
        self.wait(1)

    def agree_to_terms(self):
        self.click(*self.TERMS_CHECKBOX)
        self.wait(1)

    def continue_payment(self):
        self.click(*self.PAYMENT_CONTINUE)
        self.wait(3)

    def get_final_price(self):
        final_price = self.find(*self.FINAL_PRICE)
        return final_price.text

    def confirm_order(self):
        self.click(*self.CONFIRM_BUTTON)
        self.wait(2)

    def get_success_message(self):
        success_text = self.find(*self.SUCCESS_MESSAGE)
        return success_text.text

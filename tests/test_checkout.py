# tests/test_checkout.py

from pages.home_page import HomePage
from pages.phones_page import PhonesPage
from pages.product_page import ProductPage
from pages.laptops_page import LaptopsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_order_flow(browser):
    # NOTE: "browser" comes from pytest fixture (conftest.py)
    browser.get("https://tutorialsninja.com/demo/")
    browser.maximize_window()
    
    home_page = HomePage(browser)
    phones_page = PhonesPage(browser)
    product_page = ProductPage(browser)
    laptops_page = LaptopsPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)
    
    # Navigate to Phones and select iPhone
    home_page.goto_phones()
    phones_page.select_iphone()
    
    # Interact with iPhone gallery
    product_page.open_image_gallery()
    product_page.click_next_image(5)
    screenshot_name = product_page.take_screenshot()
    print(f"Screenshot saved as: {screenshot_name}")
    product_page.close_gallery()
    
    # Add iPhone to cart
    product_page.set_quantity(2)
    product_page.add_to_cart()
    
    # Navigate to Laptops
    home_page.hover_laptops()
    laptops_page.click_show_all()
    laptops_page.select_hp_laptop()
    
    # Set calendar date and add to cart
    product_page.set_calendar_date("December 2022")
    product_page.add_to_cart()
    
    # Go to checkout
    cart_page.open_cart()
    cart_page.proceed_to_checkout()
    
    # Complete checkout process
    checkout_page.select_guest_checkout()
    checkout_page.scroll_to_billing_details()
    checkout_page.fill_billing_details()
    checkout_page.select_country_and_region()
    checkout_page.continue_billing()
    checkout_page.continue_shipping()
    checkout_page.agree_to_terms()
    checkout_page.continue_payment()
    
    # Get final price and confirm order
    final_price = checkout_page.get_final_price()
    print(f"The final price of products is {final_price}")
    
    checkout_page.confirm_order()
    success_message = checkout_page.get_success_message()
    print(success_message)

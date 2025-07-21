# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

# Launch Chrome browser and navigate to the demo site
driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

# Navigate to "Phones & PDAs" section
phones = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(),'Phones & PDAs')]")
phones.click()

# Click on the "iPhone" product
iphone = driver.find_element(By.XPATH, "//a[normalize-space()='iPhone']")
iphone.click()
time.sleep(3)

# Click on the first product image to open gallery
first_pic = driver.find_element(By.XPATH, "//ul[@class='thumbnails']/li[1]")
first_pic.click()
time.sleep(2)

# Loop to click "Next" button in gallery 5 times
next_click = driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
for i in range(0, 5):
    next_click.click()
    time.sleep(3)

# Take a screenshot of the gallery with a random file name
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')
time.sleep(2)

# Close the gallery popup
x_button = driver.find_element(By.XPATH, "//button[@title='Close (Esc)']")
x_button.click()
time.sleep(2)

# Set product quantity to 2 and add to cart
quantity = driver.find_element(By.ID, "input-quantity")
quantity.click()
time.sleep(2)
quantity.clear()
time.sleep(1)
quantity.send_keys("2")
time.sleep(1)
add_to_cart = driver.find_element(By.XPATH, "//button[@id='button-cart']")
add_to_cart.click()
time.sleep(2)

# Navigate to Laptops & Notebooks > Show All
laptop_navbar = driver.find_element(By.XPATH, "//a[text()='Laptops & Notebooks']")
action = ActionChains(driver)
action.move_to_element(laptop_navbar).perform()
time.sleep(2)
laptop_option = driver.find_element(By.XPATH, "//a[text()='Show AllLaptops & Notebooks']")
laptop_option.click()
time.sleep(2)

# Click on the "HP LP3065" product
hp = driver.find_element(By.XPATH, "//a[text()='HP LP3065']")
hp.click()
time.sleep(2)

# Scroll into view for calendar and open it
add_to_cart_2 = driver.find_element(By.XPATH, "//button[@id='button-cart']")
add_to_cart_2.location_once_scrolled_into_view
time.sleep(2)
calendar = driver.find_element(By.XPATH, "//i[@class='fa fa-calendar']")
calendar.click()

# Select date: December 31, 2022
next_click_calendar = driver.find_element(By.XPATH, "//th[@class='next']")
month_year = driver.find_element(By.XPATH, "//th[@class='picker-switch']")
while month_year.text != 'December 2022':
    next_click_calendar.click()
    month_year = driver.find_element(By.XPATH, "//th[@class='picker-switch']")
calendar_date = driver.find_element(By.XPATH, "//td[text()='31']")
calendar_date.click()
time.sleep(1)

# Add to cart
add_to_cart_2.click()
time.sleep(2)

# Open cart and proceed to checkout
go_to_cart = driver.find_element(By.ID, "cart-total")
go_to_cart.click()
time.sleep(2)
checkout = driver.find_element(By.XPATH, "//p[@class='text-right']/a[2]")
checkout.click()
time.sleep(2)

# Select guest checkout option
guest = driver.find_element(By.XPATH, "//input[@value='guest']")
guest.click()
continue_1 = driver.find_element(By.ID, "button-account")
continue_1.click()
time.sleep(1)

# Scroll to Step 2: Billing Details
step_2 = driver.find_element(By.XPATH, "//a[text()='Step 2: Billing Details ']")
step_2.location_once_scrolled_into_view
time.sleep(1)

# Fill in billing details form
driver.find_element(By.ID, 'input-payment-firstname').send_keys('test_first_name')
driver.find_element(By.ID, 'input-payment-lastname').send_keys('test_last_name')
driver.find_element(By.ID, 'input-payment-email').send_keys('test@test.com')
driver.find_element(By.ID, 'input-payment-telephone').send_keys('012345678')
driver.find_element(By.ID, 'input-payment-address-1').send_keys('teststreet 87')
driver.find_element(By.ID, 'input-payment-city').send_keys('Bengaluru')
driver.find_element(By.ID, 'input-payment-postcode').send_keys('560098')
time.sleep(3)

# Select Country: India
country = driver.find_element(By.ID, 'input-payment-country')
dropdown_1 = Select(country)
time.sleep(2)
dropdown_1.select_by_visible_text('India')
time.sleep(2)

# Select State/Region: Karnataka
region = driver.find_element(By.ID, 'input-payment-zone')
dropdown_2 = Select(region)
time.sleep(2)
dropdown_2.select_by_visible_text('Karnataka')
time.sleep(2)

# Click Continue after billing info
continue_2 = driver.find_element(By.XPATH, '//input[@id="button-guest"]')
continue_2.click()
time.sleep(1)

# Click Continue after shipping method
continue_3 = driver.find_element(By.XPATH, '//input[@id="button-shipping-method"]')
continue_3.click()
time.sleep(1)

# Agree to Terms & Conditions
t_e = driver.find_element(By.XPATH, '//input[@name="agree"]')
t_e.click()
time.sleep(1)

# Click Continue after payment method
continue_4 = driver.find_element(By.XPATH, '//input[@id="button-payment-method"]')
continue_4.click()
time.sleep(3)

# Get final price and print it
final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
print("The final price of products is " + final_price.text)
time.sleep(2)

# Confirm the order
confirmation_button = driver.find_element(By.ID, 'button-confirm')
confirmation_button.click()
time.sleep(2)

# Print the success message
success_text = driver.find_element(By.XPATH, '//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

# Close the browser
driver.close()
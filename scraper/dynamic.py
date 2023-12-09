"""
PLEASE READ:

1. In task-2 I created it with Amazon in mind, since it is a great example of a dynamic website.
2. In task-2, an additional feature of log-in has been added where after entering username/pass & the program will carry out everything.
3. The program returns the discount %, along with the name of the product.
4. The program clicks the product from "id", "desktop-grid-1". If you do not have a grid on your Amazon homepage, you can add the visible id tag, it will work either way.
5. The amazon sign in link is specific to the code below, it works since it has the username/password input fields at the right places. However if you change site from Amazon to something else, rest of the code will need to be changed too.
"""

# Import the required libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# For task 3,imported a function that takes in value
from dataextraction import add

# Create a webdriver instance
url = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 120)

# Enterin username and password to enter the credentials
try:
    username = wait.until(EC.visibility_of_element_located(("id", "ap_email")))
    username.send_keys("your-mail")
    continue_button = driver.find_element("id", "continue")
    continue_button.click()

    password = wait.until(EC.visibility_of_element_located(("id", "ap_password")))
    password.send_keys("your-pass")
except TimeoutException:
    print("The username and password fields did not load in time")
    driver.quit()
    exit()
except NoSuchElementException:
    print("The username and password fields were not found")
    driver.quit()
    exit()

# Find the login button nd click on it
try:
    login = wait.until(EC.element_to_be_clickable(("id", "signInSubmit")))
    login.click()
except TimeoutException:
    print("The login button did not load in time")
    driver.quit()
    exit()
print("You are now logged in to the website")


# Find the product & click on it
try:
    product = wait.until(EC.element_to_be_clickable(("id", "desktop-grid-1")))
    product.click()
except TimeoutException:
    print("The product element did not load in time")
    driver.quit()
    exit()

# Find the add to cart button and click on it
try:
    add_to_cart = wait.until(EC.element_to_be_clickable(("id", "add-to-cart-button")))
    add_to_cart.click()
except TimeoutException:
    print("The add to cart button did not load in time")
    driver.quit()
    exit()

# Close the unnecessary side cart
try:
    close = wait.until(
        EC.element_to_be_clickable(("id", "attach-close_sideSheet-link"))
    )
    close.click()
except TimeoutException:
    print("The close button did not load in time")
    driver.quit()
    exit()

# Get name of product so that it can be used for task 3.
try:
    product = wait.until(EC.visibility_of_element_located(("id", "productTitle")))
    product_name = product.text
    print("The product name is", product_name)
except TimeoutException:
    print("The discount price element did not load in time")
    driver.quit()
    exit()

# Find the discount price element and get its text
try:
    discount = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                " .savingPriceOverride",
            )
        )
    )
    discount_price = discount.text
    print(f"The discount price is {discount_price}")
except TimeoutException:
    print("The discount price element did not load in time")
    driver.quit()
    exit()
except NoSuchElementException:
    print("The discount price element was not found")
    driver.quit()
    exit()

driver.quit()

# For task 3
name = [product_name]
price = [discount_price]

add(name, price)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("webdriver.chrome.driver=/Users/parth/Downloads/chromedriver_mac64")

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Test Case 1: Open the website
driver.get("https://parth-shete.github.io/Modern-Coders/")

# Explanation: The code initializes the WebDriver, navigates to the website, and opens it.

# Test Case 1: Click on the "Login" link
login_link = driver.find_element_by_id("login-link")
login_link.click()

# Test Case 2: Fill out the login form with valid credentials
username_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login-button")

username_input.send_keys("your_username")
password_input.send_keys("your_password")
login_button.click()

# Test Case 3: Verify successful login
welcome_message = driver.find_element_by_id("welcome-message").text
assert "Welcome, your_username!" in welcome_message

# Test Case 2: Check the title of the page
assert "Modern Coders" in driver.title

# Explanation: This test checks whether the title of the webpage contains "Modern Coders."

# Test Case 3: Click on the "Home" link
driver.find_element_by_link_text("Home").click()

# Explanation: This test clicks on the "Home" link in the navigation menu.

# Test Case 4: Click on the "About" link
driver.find_element_by_link_text("About").click()

# Explanation: This test clicks on the "About" link in the navigation menu.

# Test Case 5: Click on the "Services" link
driver.find_element_by_link_text("Services").click()

# Explanation: This test clicks on the "Services" link in the navigation menu.

# Test Case 6: Click on the "Projects" link
driver.find_element_by_link_text("Projects").click()

# Explanation: This test clicks on the "Projects" link in the navigation menu.

# Test Case 7: Click on the "Contact" link
driver.find_element_by_link_text("Contact").click()

# Explanation: This test clicks on the "Contact" link in the navigation menu.

# Test Case 8: Fill out and submit the contact form
driver.find_element_by_name("name").send_keys("John Doe")
driver.find_element_by_name("email").send_keys("johndoe@example.com")
driver.find_element_by_name("message").send_keys("This is a test message.")
driver.find_element_by_id("contact-submit").click()

# Explanation: This test fills out the contact form and submits it.

# Test Case 9: Verify a success message
success_message = driver.find_element_by_id("contact-success").text
assert "Your message has been sent successfully!" in success_message

# Explanation: This test verifies that a success message is displayed after submitting the contact form.

# Test Case 10: Click the "Back to Home" link
driver.find_element_by_link_text("Back to Home").click()

# Explanation: This test clicks on the "Back to Home" link to return to the home page.

# Note: The browser remains open after the test cases.

# Close the browser
driver.quit()

# Explanation: The browser is closed at the end of the script.


from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver")

chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

show_message_button = chrome_browser.find_element_by_class_name("btn-default")

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys("Testing Selenium input")

show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")
assert "Testing Selenium input" in output_message.text

chrome_browser.quit()

# pip install selenium
# pip install webdriver-manager
# https://chromedriver.storage.googleapis.com/98.0.4758.80/chromedriver_win32.zip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from config import USERNAME, PASSWORD

s = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)
browser.maximize_window()

browser.get("http://lms.ui.ac.ir/")

username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")
submit = browser.find_element(By.ID, "submit")

annonmentc = browser.find_element(By.ID, "annonmentc")
annonmentc.click()

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.click()

try:
    assert "errors" not in browser.page_source

except AssertionError:
    print("wrong username or password.")

finally:
    input("Press enter to exit..")
    browser.quit()

# pip install selenium
# pip install webdriver-manager
# https://chromedriver.storage.googleapis.com/98.0.4758.80/chromedriver_win32.zip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from config import USERNAME, PASSWORD
from meeting import join_meeting

s = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)
browser.maximize_window()

browser.get("http://lms.ui.ac.ir/")

username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")
submit = browser.find_element(By.ID, "submit")

# close announcement
annonmentc = browser.find_element(By.ID, "annonmentc")
annonmentc.click()

# login to account
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.click()

try:
    # assert success login
    assert "errors" not in browser.page_source

    # join the current meeting
    status = join_meeting(browser)
    print(status)

except AssertionError:
    print("wrong username or password.")

finally:
    input("press enter to exit..")
    browser.quit()

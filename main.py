# pip install selenium
# pip install webdriver-manager
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

input("Press enter to exit..")
browser.quit()

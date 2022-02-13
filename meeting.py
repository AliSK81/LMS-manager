import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class Meeting:
    def __init__(self, browser: Chrome):
        self.browser = browser

    def join_meeting(self):
        meetings = self.browser.find_elements(By.CSS_SELECTOR, ".newmeet a")

        for meeting in meetings:
            href = meeting.get_attribute("href")

            if "/join/" in str(href):
                meeting.click()
                return True

        return False

    def wait_progress(self):
        while True:
            try:
                self.browser.find_element(By.ID, "progressBar")
                time.sleep(10)
                self.browser.refresh()

            except NoSuchElementException:
                break

    def listen_only(self):
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.CLASS_NAME, "icon-bbb-listen").click()

    def microphone(self):
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.CLASS_NAME, "icon-bbb-unmute").click()

    def send_message(self, msg):
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.ID, "message-input").send_keys(msg)
        self.browser.find_element(By.CLASS_NAME, "icon-bbb-send").click()

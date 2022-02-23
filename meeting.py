import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from driver import Browser


class Meeting:
    def __init__(self, browser: Browser):
        self.browser = browser

    def join_meeting(self):
        meetings = self.browser.find_elements(By.CSS_SELECTOR, ".newmeet a")

        for meeting in meetings:
            href = meeting.get_attribute("href")

            if "/join/" in str(href):
                meeting.click()
                return True

        return False

    def wait_progress(self, period=10):
        while self.browser:
            try:
                self.browser.find_element(By.ID, "progressBar")
                self.browser.refresh()
                time.sleep(period)

            except NoSuchElementException:
                return True
        return False

    def listen_only(self, delay=10):
        self.browser.implicitly_wait(delay)
        self.browser.find_element(By.CLASS_NAME, "icon-bbb-listen").click()

    def unmute_mic(self, delay=10):
        self.browser.implicitly_wait(delay)
        self.browser.find_element(By.CSS_SELECTOR, "button[aria-label=Microphone]").click()
        time.sleep(2)
        self.browser.find_element(By.CLASS_NAME, "icon-bbb-thumbs_up").click()

    def send_message(self, msg, delay=10):
        self.browser.implicitly_wait(delay)
        self.browser.find_element(By.ID, "message-input").send_keys(msg)
        self.browser.find_element(By.CLASS_NAME, "icon-bbb-send").click()

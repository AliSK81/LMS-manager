from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from config import USERNAME, PASSWORD


class DriverOptions:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)


class WebDriver(DriverOptions):
    def __init__(self):
        DriverOptions.__init__(self)
        self.browser = self.__get_browser()

    def __get_browser(self):
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=self.options)
        return browser

    def load_browser(self):
        self.browser.get("http://lms.ui.ac.ir/")

    def login_account(self):
        self.browser.find_element(By.ID, "annonmentc").click()
        self.browser.find_element(By.ID, "username").send_keys(USERNAME)
        self.browser.find_element(By.ID, "password").send_keys(PASSWORD)
        self.browser.find_element(By.ID, "submit").click()
        assert "errors" not in self.browser.page_source

    def switch_newtab(self):
        currentTab = self.browser.current_window_handle
        for tab in self.browser.window_handles:
            if tab != currentTab:
                self.browser.switch_to.window(tab)

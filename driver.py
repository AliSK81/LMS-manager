from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DriverOptions(Options):
    def __init__(self):
        super().__init__()

        self.add_argument("start-maximized")
        self.add_argument("--ignore-certificate-errors")
        self.add_argument("--ignore-ssl-errors")

        self.add_argument('allow-file-access-from-files')
        self.add_argument('use-fake-device-for-media-stream')
        self.add_argument('use-fake-ui-for-media-stream')

        self.add_experimental_option("detach", True)
        self.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        self.add_experimental_option("useAutomationExtension", False)
        self.add_experimental_option("prefs", {"credentials_enable_service": False,
                                               "profile.password_manager_enabled": False})


class Browser(Chrome):
    def __init__(self):
        super().__init__(options=DriverOptions(),
                         service=Service(ChromeDriverManager(log_level=50).install()))


class WebDriver:
    def __init__(self):
        self.browser = Browser()

    def load_browser(self):
        self.browser.get("http://lms.ui.ac.ir/")

    def login_account(self, user):
        self.browser.find_element(By.ID, "annonmentc").click()
        self.browser.find_element(By.ID, "username").send_keys(user.username)
        self.browser.find_element(By.ID, "password").send_keys(user.password)
        self.browser.find_element(By.ID, "submit").click()
        assert "errors" not in self.browser.page_source

    def switch_newtab(self):
        currentTab = self.browser.current_window_handle
        for tab in self.browser.window_handles:
            if tab != currentTab:
                self.browser.switch_to.window(tab)

from time import sleep

from driver import WebDriver
from meeting import Meeting


def run(user, save_user, enter_meet, mic_on, first_msg, logger=None):
    browser = None

    try:
        log("Loading browser...", logger)

        driver = WebDriver()
        browser = driver.browser
        meeting = Meeting(browser)

        log("Opening site..", logger)

        driver.load_browser()

        log("Logging in.", logger)

        driver.login_account(user)

        log("", logger)

        if save_user:
            user.save_user()

        if not enter_meet:
            return

        if not meeting.join_meeting():
            log("No meetings found..", logger)
            return

        driver.switch_newtab()

        log("Waiting to join...", logger)

        if not meeting.wait_progress():
            return

        log("Selecting sound mode..", logger)

        sleep(2)

        if mic_on:
            meeting.unmute_mic()
        else:
            meeting.listen_only()

        log("", logger)

        sleep(2)

        if first_msg:
            meeting.send_message(first_msg)


    except AssertionError:
        log("Wrong username or password!", logger)
        if browser is not None:
            browser.quit()

    except Exception as e:
        log("Unknown error. try again!", logger)
        log(e.args[0])


def log(msg, logger=None):
    if logger:
        logger.configure(text=msg)
    print(msg)

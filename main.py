from driver import WebDriver
from meeting import Meeting


def main():
    driver = WebDriver()
    browser = driver.browser
    meeting = Meeting(browser)

    try:
        driver.load_browser()
        driver.login_account()

        if meeting.join_meeting():
            driver.switch_newtab()
            meeting.wait_progress()
            meeting.listen_only()
            # meeting.microphone()
            meeting.send_message("سلام")

        else:
            print("no sessions are running..")

    except AssertionError:
        print("wrong username or password.")

    finally:
        input("press enter to exit..")
        browser.quit()


if __name__ == "__main__":
    main()

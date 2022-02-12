from selenium.webdriver.common.by import By


def session_running(href):
    return "/join/" in str(href)


def join_meeting(browser):
    meetings = browser.find_elements(By.CSS_SELECTOR, ".newmeet a")

    for meeting in meetings:
        href = meeting.get_attribute("href")
        if session_running(href):
            meeting.click()
            # TODO select listen-only or mic modes

            return f"joining current meeting.."

    return "no running meeting found.."

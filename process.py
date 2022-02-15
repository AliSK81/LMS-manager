from time import sleep

from driver import WebDriver
from meeting import Meeting
from user import *


def run(form):
    form.msg_lbl.configure(text="Loading browser...", fg="blue")

    browser = None

    try:
        index = form.name_cbox.current()
        user = load_users()[index] if index > 0 else User(form.username_ent.get(),
                                                          form.password_ent.get(),
                                                          form.name_cbox.get())
        assert index > 0 or user.username != "" or user.username != ""

        driver = WebDriver()
        browser = driver.browser
        meeting = Meeting(browser)

        form.msg_lbl.configure(text="Opening site..", fg="purple")

        driver.load_browser()

        form.msg_lbl.configure(text="Logging in.", fg="orange")

        driver.login_account(user)

        form.msg_lbl.configure(text="")

        # browser.maximize_window()
        # browser.execute_script("window.scrollTo(0, 120)")

        if form.save_info_cbtn.get():
            save_user(user)

        if not form.enter_meet_cbtn.get():
            return

        form.msg_lbl.configure(text="Refreshing list..", fg="green")

        if not meeting.join_meeting():
            return

        driver.switch_newtab()

        form.msg_lbl.configure(text="Waiting for master...", fg="purple")

        if not meeting.wait_progress():
            return

        form.msg_lbl.configure(text="")

        sleep(2)

        if form.microphone_cbtn.get():
            meeting.unmute_mic()
        else:
            meeting.listen_only()

        sleep(5)

        if form.say_hello_cbtn.get():
            meeting.send_message("سلام")

        return

    except AssertionError:
        form.msg_lbl.configure(text="wrong username or password!", fg="red")
        if browser is not None:
            browser.quit()

    except Exception as e:
        print(e.args[0])

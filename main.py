def user_mode():
    from gui import Form
    Form().mainloop()


def developer_mode():
    import process
    from user import User

    # replace with your username and password
    USERNAME = ''
    PASSWORD = ''

    process.run(
        user=User(USERNAME, PASSWORD),
        save_user=True,
        enter_meet=True,
        mic_on=False,
        first_msg="سلام",  # None to say nothing
    )
    input("Press enter to exit..")


def hide_console():
    # # pip install pywin32
    # import win32con, win32gui
    # hide = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(hide, win32con.SW_HIDE)
    pass


if __name__ == "__main__":
    # hide_console()

    # No GUI (console log)
    # developer_mode()

    # Show GUI
    user_mode()

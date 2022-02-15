from threading import Thread
from tkinter import *
from tkinter.ttk import Combobox

import process
from user import *


class Form(Tk):
    def __init__(self):
        super().__init__()
        self.__init_from()
        self.__init_components()

    def start(self):
        Thread(target=process.run, args=[self], daemon=True).start()

    def destroy(self):
        super().destroy()
        sys.exit(0)

    def __init_from(self):
        self.title("LMS-Manager")
        self.configure(bg='#fdd741')
        self.resizable(False, False)
        self.attributes('-topmost', True)

    def __init_components(self):
        users = load_users()
        index = 0 if len(users) == 1 else 1

        Label(self, text="Name:", width=20).grid(column=0, row=0, pady=10)
        self.name_cbox = Combobox(self, width=20, values=users, textvariable=StringVar())
        self.name_cbox.grid(column=1, row=0, ipadx=2)
        self.name_cbox.current(index)

        Label(self, text="Username:", width=20).grid(column=0, row=1, pady=0)
        self.username_ent = Entry(self, width=20)
        self.username_ent.grid(column=1, row=1, ipadx=12)

        Label(self, text="Password:", width=20).grid(column=0, row=2, pady=10)
        self.password_ent = Entry(self, width=20)
        self.password_ent.grid(column=1, row=2, ipadx=12)

        self.enter_meet_cbtn = IntVar(value=1)
        self.say_hello_cbtn = IntVar(value=1)
        self.microphone_cbtn = IntVar()
        self.save_info_cbtn = IntVar()

        Checkbutton(self, text="Enter Meeting", variable=self.enter_meet_cbtn, onvalue=1, offvalue=0,
                    width=17).grid(column=0, row=5, padx=10, pady=0)
        Checkbutton(self, text="Microphone", variable=self.microphone_cbtn, onvalue=1, offvalue=0,
                    width=17).grid(column=1, row=5, padx=10)
        Checkbutton(self, text="Save Info", variable=self.save_info_cbtn, onvalue=1, offvalue=0,
                    width=17).grid(column=1, row=6, padx=10)
        Checkbutton(self, text="Say Hello", variable=self.say_hello_cbtn, onvalue=1, offvalue=0,
                    width=17).grid(column=0, row=6, padx=10, pady=10)

        Button(self, text="Login", fg="#f9faf9", bg='#522f7a', width=20,
               command=self.start).grid(column=0, row=8, padx=10, ipady=3, pady=5)

        Button(self, text="Exit", fg="#f9faf9", bg='#e44299', width=20,
               command=self.destroy).grid(column=1, row=8, padx=10, ipady=3)

        self.msg_lbl = Label(self, text="", bg="#fdd741")
        self.msg_lbl.grid(column=0, row=9, ipadx=5, ipady=5)

"""main"""

import os
import tkinter as tk

from PIL import Image, ImageTk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk


def button_image(icon, size=(20, 20)):
    """button image"""

    icons = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
    image = Image.open(os.path.join(icons, icon)).resize(size)
    image = ImageTk.PhotoImage(image)
    return image


class App(ttk.Window):
    """App"""

    def __init__(self):
        super().__init__()

        self.title("LockByte")
        self.geometry("700x600")
        self.style.theme_use("flatly")
        self.resizable(False, False)

        # set grid layout 2x2
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # application variables
        self.term_var = ttk.StringVar(value="md")

        # icons
        self.header_icon = button_image("checkup.png", (50, 50))
        self.setting_icon = button_image("settings.png")
        self.password_icon = button_image("passwords.png")
        self.checkup_icon = button_image("checkup.png")

        # header
        self.header_frame = ttk.Frame(self, padding=20, style="primary.TFrame")
        self.create_header_frame()

        # create navigation frame
        self.navigation_frame = ttk.Frame(self, style="primary.TFrame")
        self.create_navigation_frame()

        # create passwords frame
        self.passwords_frame = ttk.Frame(self)
        self.create_passwords_frame()

        # create Checkup frame
        self.checkup_frame = ttk.Frame(self)
        self.create_checkup_frame()

        # create Setting frame
        self.settings_frame = ttk.Frame(self)
        self.create_settings_frame()

        # select default frame
        self.select_frame_by_name("passwords")

    def select_frame_by_name(self, name):
        """select frame by name"""

        if name == "passwords":
            self.passwords_frame.grid(
                row=1, column=1, sticky=NSEW, padx=(2, 2), pady=(2, 2)
            )
        else:
            self.passwords_frame.grid_forget()

        if name == "checkup":
            self.checkup_frame.grid(
                row=1, column=1, sticky=NSEW, padx=(2, 2), pady=(2, 2)
            )
        else:
            self.checkup_frame.grid_forget()

        if name == "settings":
            self.settings_frame.grid(
                row=1, column=1, sticky=NSEW, padx=(2, 2), pady=(2, 2)
            )
        else:
            self.settings_frame.grid_forget()

    def password_button_event(self):
        """home button event"""
        self.select_frame_by_name("passwords")

    def checkup_button_event(self):
        """frame 2 button event"""
        self.select_frame_by_name("checkup")

    def setting_button_event(self):
        """frame 3 button event"""
        self.select_frame_by_name("settings")

    def create_header_frame(self):
        """create_header_frame"""

        self.header_frame.grid(row=0, column=0, columnspan=2, sticky=EW)
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)

        header_logo = ttk.Label(
            self.header_frame, image=self.header_icon, style="primary.TLabel"
        )
        header_logo.grid(row=0, column=0, padx=10, pady=10)

        header_text = ttk.Label(
            self.header_frame,
            text="LockByte",
            font=("TkDefaultFixed", 30),
            anchor=E,
        )
        header_text.grid(row=0, column=1, padx=10, pady=10)

    def create_navigation_frame(self):
        """create_navigation_frame"""

        self.navigation_frame.grid(row=1, column=0, sticky=NSEW)
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.passwords_button = ttk.Button(
            self.navigation_frame,
            text="Passwords",
            image=self.password_icon,
            command=self.password_button_event,
            compound="left",
        )

        self.passwords_button.grid(row=1, column=0, sticky="ew")

        self.checkup_button = ttk.Button(
            self.navigation_frame,
            text="Checkup",
            image=self.checkup_icon,
            command=self.checkup_button_event,
            compound="left",
        )
        self.checkup_button.grid(row=2, column=0, sticky="ew")

        self.settings_button = ttk.Button(
            self.navigation_frame,
            text="Settings",
            image=self.setting_icon,
            command=self.setting_button_event,
            compound="left",
        )
        self.settings_button.grid(row=3, column=0, sticky="ew")

    def create_passwords_frame(self):
        """labelframe"""

        self.passwords_frame.grid_rowconfigure(0, weight=1)
        self.passwords_frame.grid_columnconfigure(2, weight=1)

        search_frame = ttk.Frame(self.passwords_frame)
        search_frame.pack(fill=X, expand=YES, pady=15)
        term_ent = ttk.Entry(search_frame, textvariable=self.term_var)
        term_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        search_btn = ttk.Button(
            master=search_frame,
            text="Search",
            bootstyle=OUTLINE,
            width=8,
        )
        search_btn.pack(side=LEFT, padx=5)

    def create_checkup_frame(self):
        """labelframe"""

        # set grid layout 1x4
        self.checkup_frame.grid_rowconfigure(3, weight=1)
        self.checkup_frame.grid_columnconfigure(0, weight=1)

        search_frame = ttk.Frame(self.checkup_frame, bootstyle="light")
        search_frame.grid(row=0, column=0, sticky=EW, padx=2, pady=2)

        path_lbl = ttk.Label(
            search_frame,
            text="Check All Password",
            font=("Helvetica", 18),
        )
        path_lbl.pack(padx=20, pady=20)

        search_btn = ttk.Button(search_frame, text="Check", width=10)
        search_btn.pack(pady=20, padx=20)

        search_frame = ttk.Frame(self.checkup_frame, height=150)
        search_frame.grid(row=1, column=0, sticky=EW, padx=2, pady=2)

        container = ttk.Labelframe(self.checkup_frame, text="Check Password Strenght")
        container.grid(row=2, column=0, sticky=EW, padx=50, pady=2)

        ent = ttk.Entry(container, textvariable="password")
        ent.pack(padx=100, pady=20, fill=X)

        lbl = ttk.Button(master=container, text="password", width=10)
        lbl.pack(padx=20, pady=20)

        progressbar = ttk.Progressbar(
            master=self.checkup_frame, mode=INDETERMINATE, bootstyle=(STRIPED, SUCCESS)
        )
        progressbar.grid(row=3, column=0, sticky=EW, padx=2, pady=2)

    def create_settings_frame(self):
        """labelframe"""

        self.settings_frame.grid_rowconfigure(0, weight=1)
        self.settings_frame.grid_columnconfigure(1, weight=1)

        search_frame = ttk.Frame(self.settings_frame)
        search_frame.pack(fill=X, expand=YES, pady=15)
        term_ent = ttk.Entry(search_frame, textvariable=self.term_var)
        term_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        search_btn = ttk.Button(
            search_frame,
            text="Search",
            bootstyle=OUTLINE,
            width=8,
        )
        search_btn.pack(side=LEFT, padx=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()

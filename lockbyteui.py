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
        self.geometry("700x450")
        self.style.theme_use("flatly")

        # set grid layout 2x2
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # icons
        self.header_icon = button_image("checkup.png", (50, 50))
        self.setting_icon = button_image("settings.png")
        self.password_icon = button_image("passwords.png")
        self.checkup_icon = button_image("checkup.png")

        # header
        hdr_frame = ttk.Frame(self, padding=20, style="primary.TFrame")
        hdr_frame.grid(row=0, column=0, columnspan=2, sticky=EW)
        hdr_frame.grid_rowconfigure(0, weight=1)
        hdr_frame.grid_columnconfigure(1, weight=1)

        hdr_label = ttk.Label(hdr_frame, image=self.header_icon, style="primary.TLabel")
        hdr_label.grid(row=0, column=0, padx=10, pady=10)

        logo_text = ttk.Label(
            hdr_frame, text="LockByte", font=("TkDefaultFixed", 30), anchor=E
        )
        logo_text.grid(row=0, column=1, padx=10, pady=10)

        # create navigation frame
        self.navigation_frame = ttk.Frame(self, style="primary.TFrame")
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

        # create passwords frame
        self.passwords_frame = ttk.Frame(self)
        # self.passwords_frame.grid_columnconfigure(0, weight=1)

        self.passwords_frame_label_image = ttk.Label(
            self.passwords_frame, text="Password", image=button_image("settings.png")
        )
        self.passwords_frame_label_image.grid(row=0, column=0, padx=20, pady=10)

        self.password_frame_button_1 = ttk.Button(
            self.passwords_frame, text="Password", image=button_image("settings.png")
        )
        self.password_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        # create Checkup frame
        self.checkup_frame = ttk.Frame(self)

        # create Setting frame
        self.settings_frame = ttk.Frame(self)

        # select default frame
        self.select_frame_by_name("passwords")

    def select_frame_by_name(self, name):
        """select frame by name"""

        if name == "passwords":
            self.passwords_frame.grid(row=1, column=1, sticky=NSEW, pady=(25, 0))
        else:
            self.passwords_frame.grid_forget()

        if name == "checkup":
            self.checkup_frame.grid(row=1, column=1, sticky=NSEW, pady=(25, 0))
        else:
            self.checkup_frame.grid_forget()

        if name == "settings":
            self.settings_frame.grid(row=1, column=1, sticky=NSEW, pady=(25, 0))
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


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""main"""

import tkinter as tk


def password_menu(window, main_frame):
    """Open"""


def checkup_menu(window, main_frame):
    """Open"""


def settings_menu(window, main_frame):
    """Open"""


def main():
    """main"""

    window = tk.Tk()
    window.title("Studio Nut")
    window.iconbitmap("")
    window.resizable(False, False)
    window.geometry("600x400")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    menu_frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    main_frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    passwords_btn = tk.Button(
        menu_frame, text="Password", command=lambda: password_menu(window, main_frame)
    )

    checkup_btn = tk.Button(
        menu_frame, text="Checkup", command=lambda: checkup_menu(window, main_frame)
    )

    settings_btn = tk.Button(
        menu_frame, text="Settings", command=lambda: settings_menu(window, main_frame)
    )

    passwords_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    checkup_btn.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    settings_btn.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    menu_frame.grid(row=0, column=0, sticky="ns")

    main_frame.grid(row=0, column=1)

    window.mainloop()


main()

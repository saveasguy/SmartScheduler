import tkinter as tk

import scheduler.views as views


def main():
    app = tk.Tk()
    login = views.LoginView(app, None)
    login.pack()
    app.mainloop()


if __name__ == "__main__":
    main()

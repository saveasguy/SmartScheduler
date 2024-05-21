import tkinter as tk


class ILoginController:
    """Interface class for login controller,
    which requires to implement on_auth method
    """

    def on_auth(self, view) -> None:
        raise NotImplementedError()


class LoginView(tk.Frame):
    def __init__(self, parent, controller: ILoginController):
        tk.Frame.__init__(self, parent)

        # Data displayed in GUI
        self.company = tk.StringVar()
        self.user = tk.StringVar()
        self.password = tk.StringVar()
        self.error = tk.StringVar()

        # GUI setup
        company_label = tk.Label(self, text="Company")
        company_label.pack(anchor="center")
        company_entry = tk.Entry(self, textvariable=self.company)
        company_entry.pack(anchor="center")

        user_label = tk.Label(self, text="Username")
        user_label.pack()
        user_entry = tk.Entry(self, textvariable=self.user)
        user_entry.pack()

        password_label = tk.Label(self, text="Password")
        password_label.pack()
        password_entry = tk.Entry(self, show="*", textvariable=self.password)
        password_entry.pack()

        login_button = tk.Button(
            self, text="Login", command=lambda: controller.on_auth(self)
        )
        login_button.pack()

        error_label = tk.Label(self, textvariable=self.error)
        error_label.pack()

    def handle_authorization_error(self):
        self.error.set("Failed to authorize!")

import tkinter as tk


class ILoginController:
    def on_auth(self, login_view) -> None:
        raise NotImplementedError()


class LoginView(tk.Frame):
    def __init__(self, parent, login_controller: ILoginController):
        tk.Frame.__init__(self, parent)

        company_label = tk.Label(self, text="Company")
        company_label.pack()
        company = ""
        company_entry = tk.Entry(self, textvariable=company)
        company_entry.pack()

        user = ""
        user_label = tk.Label(self, text="Username")
        user_label.pack()
        self.user_entry = tk.Entry(self, textvariable=user)
        self.user_entry.pack()

        password = ""
        password_label = tk.Label(self, text="Password")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*", textvariable=password)
        self.password_entry.pack()

        login_button = tk.Button(self, text="Login")
        login_button.pack()

        self.error = ""
        self.error_label = tk.Label(self, textvariable=self.error)
        self.error_label.pack()

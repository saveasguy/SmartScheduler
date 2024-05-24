import tkinter as tk
import tkinter.ttk as ttk

from typing import List


class ILoginController:
    """Interface class for login controller,
    which requires to implement on_auth method
    """

    def on_auth(self, view):
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


class IBoardController:
    def get_project_names(self) -> List[str]:
        raise NotImplementedError()

    def get_board_names_by_project_name(self, project_name: str) -> List[str]:
        raise NotImplementedError()

    def on_choose_board(self, project: str, board: str):
        raise NotImplementedError()


class BoardView(tk.Frame):
    def __init__(self, parent, controller: IBoardController):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.selected_project = None
        self.selected_board = None

        self.projects_combo = ttk.Combobox(
            self,
            values=[],
            textvariable=self.selected_project,
        )
        self.projects_combo.pack()
        self.projects_combo.bind(
            "<<ComboboxSelected>>", lambda _: self.on_project_choice()
        )
        self.boards_combo = ttk.Combobox(
            self, values=[], textvariable=self.selected_board
        )
        self.boards_combo.pack()
        choose_button = tk.Button(
            self,
            text="Choose",
            command=lambda: self.controller.on_choose_board(
                self.selected_project, self.selected_board
            ),
        )
        choose_button.pack()

    def update_projects_list(self):
        self.projects_combo.config(values=self.controller.get_project_names())
        self.boards_combo.config(values=[])

    def on_project_choice(self):
        """Display list of boards connected to project"""
        self.boards_combo.config(
            values=self.controller.get_board_names_by_project_name(
                self.selected_project
            )
        )

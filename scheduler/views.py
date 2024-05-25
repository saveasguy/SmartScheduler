from typing import List

import customtkinter as tk


class ILoginController:
    """Interface class for login controller,
    which requires to implement on_auth method
    """

    def on_auth(self, view):
        raise NotImplementedError()


class LoginView(tk.CTkFrame):
    def __init__(self, parent, controller: ILoginController):
        tk.CTkFrame.__init__(self, parent)

        HEADER2_FONT = tk.CTkFont(size=22)
        PARAGRAPH_FONT = tk.CTkFont(size=16)

        # Data displayed in GUI
        self.company = tk.StringVar()
        self.user = tk.StringVar()
        self.password = tk.StringVar()
        self.error = tk.StringVar()

        # GUI setup
        company_label = tk.CTkLabel(self, text="Company", font=HEADER2_FONT)
        company_label.place(rely=0.1, relwidth=1)

        company_entry = tk.CTkEntry(
            self, textvariable=self.company, font=PARAGRAPH_FONT
        )
        company_entry.place(rely=0.16, relx=0.25, relwidth=0.5)

        user_label = tk.CTkLabel(self, text="Username", font=HEADER2_FONT)
        user_label.place(rely=0.26, relwidth=1)
        user_entry = tk.CTkEntry(
            self, textvariable=self.user, font=PARAGRAPH_FONT
        )
        user_entry.place(rely=0.32, relx=0.25, relwidth=0.5)

        password_label = tk.CTkLabel(self, text="Password", font=HEADER2_FONT)
        password_label.place(rely=0.42, relwidth=1)
        password_entry = tk.CTkEntry(
            self, show="*", textvariable=self.password, font=PARAGRAPH_FONT
        )
        password_entry.place(rely=0.48, relx=0.25, relwidth=0.5)

        login_button = tk.CTkButton(
            self,
            text="Login",
            command=lambda: controller.on_auth(self),
            font=PARAGRAPH_FONT,
        )
        login_button.place(rely=0.58, relx=0.3, relwidth=0.4)

        error_label = tk.CTkLabel(
            self,
            textvariable=self.error,
            font=PARAGRAPH_FONT,
            text_color="red",
        )
        error_label.place(rely=0.68, relwidth=1)

    def handle_authorization_error(self):
        self.error.set("Failed to authorize!")


class IBoardController:
    def get_project_names(self) -> List[str]:
        raise NotImplementedError()

    def get_board_names_by_project_name(self, project_name: str) -> List[str]:
        raise NotImplementedError()

    def on_choose_board(self, project: str, board: str):
        raise NotImplementedError()


class BoardView(tk.CTkFrame):
    def __init__(self, parent, controller: IBoardController):
        tk.CTkFrame.__init__(self, parent)

        HEADER2_FONT = tk.CTkFont(size=22)
        PARAGRAPH_FONT = tk.CTkFont(size=16)

        self.controller = controller
        self.selected_project = None
        self.selected_board = None

        # GUI setup
        projects_label = tk.CTkLabel(self, text="Project", font=HEADER2_FONT)
        projects_label.place(rely=0.2, relwidth=1)
        self.projects_combo = tk.CTkComboBox(
            self,
            values=controller.get_project_names(),
            command=lambda choice: self.on_project_choice(choice),
            font=PARAGRAPH_FONT,
            dropdown_font=PARAGRAPH_FONT,
        )
        self.projects_combo.set("")
        self.projects_combo.place(rely=0.26, relx=0.3, relwidth=0.4)

        boards_label = tk.CTkLabel(self, text="Board", font=HEADER2_FONT)
        boards_label.place(rely=0.36, relwidth=1)
        self.boards_combo = tk.CTkComboBox(
            self,
            values=[],
            command=lambda choice: self.on_board_choice(choice),
            font=PARAGRAPH_FONT,
            dropdown_font=PARAGRAPH_FONT,
        )
        self.boards_combo.set("")
        self.boards_combo.place(
            rely=0.42,
            relx=0.3,
            relwidth=0.4,
        )

        choose_button = tk.CTkButton(
            self,
            text="Choose",
            command=lambda: self.controller.on_choose_board(
                self.selected_board
            ),
            font=HEADER2_FONT,
        )
        choose_button.place(rely=0.52, relx=0.3, relwidth=0.4)

    def update_projects_list(self):
        self.projects_combo.configure(
            values=self.controller.get_project_names()
        )
        self.boards_combo.configure(values=[])

    def on_project_choice(self, choice):
        """Display list of boards connected to project"""
        self.selected_project = choice
        self.boards_combo.configure(
            values=self.controller.get_board_names_by_project_name(
                self.selected_project
            )
        )

    def on_board_choice(self, choice):
        self.selected_board = choice

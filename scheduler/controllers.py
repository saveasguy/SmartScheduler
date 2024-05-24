from customtkinter import CTk
from itertools import chain

from scheduler import models
from scheduler import views
from typing import List


class IApp(CTk):
    def __init__(self):
        super().__init__()

    def get_model(self) -> models.AppLogicModel:
        raise NotImplementedError()

    def show_view(self, id: str):
        """Show the view with the given id

        :param id: Id of the view
        :type id: str
        """
        raise NotImplementedError()


class LoginController(views.ILoginController):
    def __init__(self, app: IApp):
        self.app = app

    def on_auth(self, view: views.LoginView):
        """Callback which is invoked when login button is pressed.
        If login failed, call views method to display authorization failure.
        Otherwise show page allowing to choose project and board

        :param view: Login page, which should call this method.
        :type view: views.LoginView
        """
        try:
            self.app.get_model().auth(
                view.user.get(),
                view.password.get(),
                view.company.get(),
            )
        except ValueError:
            view.handle_authorization_error()
            return
        self.app.show_view("boards")


class BoardController(views.IBoardController):
    def __init__(self, app: IApp):
        self.app = app
        self.projects: List[models.Project] = []
        self.boards: List[models.Board] = []

    def get_project_names(self) -> List[str]:
        self.projects = self.app.get_model().get_projects()
        return [prj.title for prj in self.projects]

    def get_board_names_by_project_name(self, project_name: str) -> List[str]:
        found_projects = [
            prj for prj in self.projects if prj.title == project_name
        ]
        if len(found_projects) != 1:
            raise RuntimeError(
                "Zero projects found or unexpected projects with the same name"
            )
        self.boards = self.app.get_model().get_boards_by_project(
            found_projects[0]
        )
        return [board.title for board in self.boards]

    def on_choose_board(self, board_name: str):
        found_boards = [
            board for board in self.boards if board.title == board_name
        ]
        if len(found_boards) != 1:
            raise RuntimeError(
                "Zero boards found or unexpected boards with the same name"
            )
        all_tasks = chain.from_iterable(
            self.app.get_model().get_tasks_by_board(found_boards[0])
        )
        print("\n".join(task.title for task in all_tasks))

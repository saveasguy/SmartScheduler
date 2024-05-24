from tkinter import Tk

from scheduler import models
from scheduler import views
from typing import List


class IApp(Tk):
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
        self.app.event_generate("<<UpdateProjectList>>", when="tail")
        self.app.show_view("project_board")


class BoardController(views.IProjectBoardController):
    def __init__(self, app: IApp):
        self.app = app
        self.projects: List[models.Project] = []
        self.boards: List[models.Board] = []

    def get_project_names(self) -> List[str]:
        self.projects = self.app.get_model().get_projects()
        return [prj.id for prj in self.projects]

    def get_board_names_by_project_name(self, project_name: str) -> List[str]:
        self.boards = self.app.get_model().get_boards_by_project()
        return [board.id for board in self.boards]

    def on_choose_board(self, project: str, board: str):
        print("Great!")

from itertools import chain
from typing import List

from customtkinter import CTk

from scheduler import models, views


class IApp(CTk):
    def __init__(self):
        super().__init__()

    def get_model(self) -> models.AppLogicModel:
        raise NotImplementedError()

    def show_view(self, id: str):
        """Show the view with the given id.

        :param id: Id of the view
        :type id: str
        """
        raise NotImplementedError()


class LoginController(views.ILoginController):
    def __init__(self, app: IApp):
        self.app = app

    def on_auth(self, view: views.LoginView):
        """Callback which is invoked when login button is pressed. If login
        failed, call views method to display authorization failure. Otherwise
        show page allowing to choose project and board.

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


def find_by_title(
    entities: List[models.Project | models.Board], title: str
) -> models.Project | None:
    """Get project with a name mathes the given one.

    :param projects: list of projects
    :type projects: List[models.Project]
    :param project_name: searched project_name
    :type project_name: str
    :raises RuntimeError: raises when there are two projects with the
        same name
    """
    found_projects = [ent for ent in entities if ent.title == title]
    if len(found_projects) != 1:
        raise RuntimeError(
            "No projects found or unexpected projects having the same names"
        )
    return found_projects[0]


class BoardController(views.IBoardController):
    def __init__(self, app: IApp):
        self.app = app
        self.projects: List[models.Project] = []
        self.boards: List[models.Board] = []

    def get_project_names(self) -> List[str]:
        self.projects = self.app.get_model().get_projects()
        return [prj.title for prj in self.projects]

    def get_board_names_by_project_name(
        self, view: views.BoardView, project_name: str
    ) -> List[str]:
        try:
            self.boards = self.app.get_model().get_boards_by_project(
                find_by_title(self.projects, project_name)
            )
        except Exception:
            view.display_internal_error()
            return []
        return [board.title for board in self.boards]

    def on_choose_board(self, view: views.BoardView, board_name: str):
        try:
            all_tasks = chain.from_iterable(
                self.app.get_model().get_tasks_by_board(
                    find_by_title(self.boards, board_name)
                )
            )
        except Exception:
            view.display_internal_error()
            return
        print("\n".join(task.title for task in all_tasks))

from scheduler import controllers
from scheduler import models
from scheduler import views


class App(controllers.IApp):
    def __init__(self):
        super().__init__()
        self.title("Smart Scheduler")
        self.geometry("500x500")

        self.model = models.AppLogicModel()
        self.views = {}

        self.views["login"] = views.LoginView(
            self, controllers.LoginController(self)
        )
        self.views["login"].grid(row=0, column=0, sticky="nsew")

        project_board_view = views.BoardView(
            self, controllers.BoardController(self)
        )
        project_board_view.grid(row=0, column=0, sticky="nsew")
        self.bind(
            "<<UpdateProjectList>>",
            lambda _: project_board_view.update_projects_list(),
        )
        self.views["project_board"] = project_board_view

        self.show_view("login")

    def get_model(self) -> models.AppLogicModel:
        return self.model

    def show_view(self, id: str):
        return self.views[id].tkraise()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

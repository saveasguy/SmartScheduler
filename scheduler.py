from scheduler import controllers
from scheduler import models
from scheduler import views


class App(controllers.IApp):
    def __init__(self):
        super().__init__()
        self.title("Smart Scheduler")
        self.geometry("300x300")

        self.model = models.AppLogicModel()
        self.login_view = views.LoginView(
            self, controllers.LoginController(self)
        )
        self.login_view.pack()

    def get_model(self) -> models.AppLogicModel:
        return self.model


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

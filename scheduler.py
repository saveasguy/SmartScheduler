from customtkinter import CTkFrame

from scheduler import controllers, models, views


class App(controllers.IApp):
    def __init__(self):
        super().__init__()
        self.title("Smart Scheduler21")
        self.minsize(512, 512)

        self.frame: CTkFrame | None = None
        self.model = models.AppLogicModel()
        self.views = {}
        self.controllers = {}

        self.views["login"] = views.LoginView
        self.controllers["login"] = controllers.LoginController(self)

        self.views["boards"] = views.BoardView
        self.controllers["boards"] = controllers.BoardController(self)

        self.show_view("login")

    def get_model(self) -> models.AppLogicModel:
        return self.model

    def show_view(self, id: str):
        view_cls = self.views[id]
        controller = self.controllers[id]
        if self.frame:
            self.frame.pack_forget()
            self.frame.destroy()
        self.frame = view_cls(self, controller)
        self.frame.pack(fill="both", expand=True)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

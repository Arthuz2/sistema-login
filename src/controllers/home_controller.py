from config.database import Database

class HomeController:
    def __init__(self, root):
        self.root = root
        self.db = Database()

    def home_view(self, username: str) -> None:
        if self.db.isAdmin(username):
            from src.controllers.admin_controller import AdminController
            AdminController(self.root).admin_view()
        else:
            from src.controllers.task_controller import TaskController
            TaskController(self.root).task_view(username)

    def go_to_login(self) -> None:
        from src.controllers.login_controller import LoginController
        LoginController(self.root).login_view()

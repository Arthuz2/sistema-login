from config.database import Database

class HomeController:
    def __init__(self, root):
        self.root = root
        self.db = Database()

    def home_view(self, username: str) -> None:
        from src.views.home_view import HomeView
        self.root.clear_screen()
        self.root.title("Início")

        users = self.db.getUsers() if self.db.isAdmin(username) else None
        HomeView(self.root, username=username, on_logout=self.go_to_login, users=users)

    def go_to_login(self) -> None:
        from src.controllers.login_controller import LoginController
        LoginController(self.root).login_view()

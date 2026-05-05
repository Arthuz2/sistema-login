from tkinter import messagebox
from config.database import Database
class LoginController:
    def __init__(self, root):
        self.root = root
        self.db = Database()

    def login_view(self) -> None:
        from src.views.login_view import LoginView
        self.root.clear_screen()
        self.root.title("Login")

        LoginView(self.root, on_login=self.login, on_register=self.go_to_register)

    def login(self, username: str, password: str):
        if not username or not password:
          return messagebox.showinfo("Login", "Credenciais não podem ser vazias!", icon="error")

        if not self.validate_credentials(username, password):
          return messagebox.showinfo("Login", "Credenciais inválidas!", icon="error", detail= "Verifique seu usuário e senha e tente novamente.")

        messagebox.showinfo("Login", "Entrada realizada com sucesso!")
        from src.controllers.home_controller import HomeController
        HomeController(self.root).home_view(username)


    def go_to_register(self) -> None:
        from src.controllers.register_controller import RegisterController
        RegisterController(self.root).register_view()

    def validate_credentials(self, username: str, password: str) -> bool:
        passwordHash = self.db.hashPassword(password)
        for user in self.db.getUsers():
            if user["username"] == username and user["password"] == passwordHash:
                return True
        return False

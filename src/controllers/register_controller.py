from tkinter import messagebox
from config.database import Database

class RegisterController:
    def __init__(self, root):
        self.root = root
        self.db = Database('data/db.json')

    def register_view(self) -> None:
        from src.views.register_view import RegisterView
        self.root.clear_screen()
        self.root.title("Registrar")
        RegisterView(self.root, on_register=self.register, on_back=self.go_to_login)

    def register(self, username: str, password: str):
        if not username or not password:
            return messagebox.showinfo("Registro", "Credenciais não podem ser vazias!", icon="error")

        for user in self.db.getUsers():
            if user["username"] == username:
                return messagebox.showinfo("Registro", "Usuário já existe!", icon="error")

        self.db.addUser(username, password)
        messagebox.showinfo("Registro", "Usuário registrado com sucesso! Faça login para continuar.")
        self.go_to_login()

    def go_to_login(self) -> None:
        from src.controllers.login_controller import LoginController
        LoginController(self.root).login_view()

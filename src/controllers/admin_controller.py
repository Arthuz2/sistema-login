from tkinter import messagebox
from config.database import Database

class AdminController:
    def __init__(self, root):
        self.root = root
        self.db = Database()

    def admin_view(self) -> None:
        from src.views.admin.admin_view import AdminView
        self.root.clear_screen()
        self.root.title("Painel Admin")

        users = self.db.getUsers()

        AdminView(
            self.root,
            users=users,
            on_logout=self.go_to_login,
            on_delete=self.delete_user,
            on_view_tasks=self.view_user_tasks,
        )

    def delete_user(self, user_id: int, username: str) -> None:
        confirm = messagebox.askyesno(
            "Excluir Usuário",
            f"Tem certeza que deseja excluir o usuário '{username}'?\nTodas as tarefas dele serão removidas.",
        )
        if confirm:
            self.db.deleteUser(user_id)
            messagebox.showinfo("Admin", "Usuário excluído com sucesso!")
            self.admin_view()

    def view_user_tasks(self, user_id: int, username: str) -> None:
        from src.views.admin.admin_task_modal import AdminTaskModal
        tasks = self.db.getTasksByUser(user_id)
        AdminTaskModal(self.root, username=username, tasks=tasks)

    def go_to_login(self) -> None:
        from src.controllers.login_controller import LoginController
        LoginController(self.root).login_view()

from tkinter import messagebox
from config.database import Database


class TaskController:
    def __init__(self, root):
        self.root = root
        self.db = Database()

    def task_view(self, username: str) -> None:
        from src.views.task_view import TaskView
        self.root.clear_screen()
        self.root.title("Minhas Tarefas")

        user = self.db.getUserByUsername(username)
        tasks = self.db.getTasksByUser(user["id"]) if user else []

        TaskView(
            self.root,
            username=username,
            tasks=tasks,
            on_logout=self.go_to_login,
            on_add=lambda title, desc: self.add_task(username, title, desc),
            on_toggle=lambda task_id: self.toggle_task(username, task_id),
            on_delete=lambda task_id: self.delete_task(username, task_id),
            on_edit=lambda task_id, title, desc: self.edit_task(username, task_id, title, desc),
        )

    def add_task(self, username: str, title: str, description: str):
        if not title.strip():
            return messagebox.showinfo("Tarefa", "O título não pode ser vazio!", icon="error")
        user = self.db.getUserByUsername(username)
        self.db.addTask(title.strip(), description.strip(), user["id"])
        self.task_view(username)

    def edit_task(self, username: str, task_id: int, title: str, description: str):
        if not title.strip():
            return messagebox.showinfo("Tarefa", "O título não pode ser vazio!", icon="error")
        self.db.updateTask(task_id, title.strip(), description.strip())
        self.task_view(username)

    def toggle_task(self, username: str, task_id: int) -> None:
        self.db.toggleTask(task_id)
        self.task_view(username)

    def delete_task(self, username: str, task_id: int) -> None:
        confirm = messagebox.askyesno("Excluir Tarefa", "Tem certeza que deseja excluir esta tarefa?")
        if confirm:
            self.db.deleteTask(task_id)
            self.task_view(username)

    def go_to_login(self) -> None:
        from src.controllers.login_controller import LoginController
        LoginController(self.root).login_view()

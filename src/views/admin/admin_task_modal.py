import customtkinter as ctk

class AdminTaskModal:
    def __init__(self, root, username, tasks):
        dialog = ctk.CTkToplevel(root)
        dialog.title(f"Tarefas de {username}")
        dialog.geometry("600x420")
        dialog.lift()
        dialog.focus_force()
        dialog.after(100, dialog.grab_set)

        ctk.CTkLabel(
            dialog,
            text=f"Tarefas de {username}",
            font=("Arial", 16, "bold"),
        ).pack(pady=(20, 14))

        if not tasks:
            ctk.CTkLabel(
                dialog,
                text="Este usuário não possui tarefas.",
                font=("Arial", 13),
                text_color="gray60",
            ).pack(pady=20)
            return

        done_count = sum(1 for t in tasks if t.get("done", False))
        ctk.CTkLabel(
            dialog,
            text=f"{done_count}/{len(tasks)} tarefas concluídas",
            font=("Arial", 11),
            text_color="gray50",
        ).pack(anchor="e", padx=20)

        table = ctk.CTkFrame(dialog, corner_radius=10, border_width=1, border_color="#3a3a4a")
        table.pack(fill="both", expand=True, padx=20, pady=(6, 20))

        h_row = ctk.CTkFrame(table, fg_color="#252540", corner_radius=8, height=36)
        h_row.pack(fill="x", padx=8, pady=(8, 4))
        ctk.CTkLabel(h_row, text="Status", font=("Arial", 12, "bold"), width=90).pack(side="left", padx=(12, 0))
        ctk.CTkLabel(h_row, text="Título", font=("Arial", 12, "bold"), width=180).pack(side="left", padx=12)
        ctk.CTkLabel(h_row, text="Descrição", font=("Arial", 12, "bold")).pack(side="left", padx=12)

        scrollable = ctk.CTkScrollableFrame(table, fg_color="transparent", corner_radius=0)
        scrollable.pack(fill="both", expand=True, padx=4, pady=(0, 4))

        for task in tasks:
            done = task.get("done", False)
            row = ctk.CTkFrame(scrollable, fg_color="#2b2b3b", corner_radius=6, height=38)
            row.pack(fill="x", pady=2)
            row.pack_propagate(False)

            ctk.CTkLabel(
                row,
                text="Concluída" if done else "Pendente",
                font=("Arial", 11, "bold"),
                text_color="#27ae60" if done else "#e67e22",
                width=90,
                anchor="w",
            ).pack(side="left", padx=(12, 0))

            ctk.CTkLabel(
                row,
                text=task["title"],
                font=("Arial", 12),
                text_color="gray55" if done else "white",
                width=180,
                anchor="w",
            ).pack(side="left", padx=12)

            ctk.CTkLabel(
                row,
                text=task.get("description", ""),
                font=("Arial", 11),
                text_color="gray60",
                anchor="w",
            ).pack(side="left", padx=12)

import customtkinter as ctk

class TaskView:
    def __init__(self, root, username, tasks, on_logout, on_add, on_toggle, on_delete, on_edit):
        self.root = root
        self.on_add = on_add
        self.on_toggle = on_toggle
        self.on_delete = on_delete
        self.on_edit = on_edit

        header = ctk.CTkFrame(root, height=56, corner_radius=0, fg_color="#1a2035")
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="Sistema de Tarefas",
            font=("Arial", 15, "bold"),
            text_color="gray70",
        ).pack(side="left", padx=24)

        header_right = ctk.CTkFrame(header, height=56, corner_radius=0, fg_color="transparent")
        header_right.pack(side="right")

        ctk.CTkLabel(
            header_right,
            text=f"Olá, {username}!",
            font=("Arial", 13),
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            header_right,
            text="Sair",
            width=76,
            height=32,
            corner_radius=8,
            fg_color="#c0392b",
            hover_color="#e74c3c",
            font=("Arial", 12, "bold"),
            command=on_logout,
        ).pack(side="right", padx=24, pady=12)

        content = ctk.CTkFrame(root, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=36, pady=24)

        top_row = ctk.CTkFrame(content, fg_color="transparent")
        top_row.pack(fill="x", pady=(0, 14))

        ctk.CTkLabel(
            top_row,
            text="Minhas Tarefas",
            font=("Arial", 17, "bold"),
        ).pack(side="left")

        ctk.CTkButton(
            top_row,
            text="+ Adicionar Tarefa",
            width=160,
            height=36,
            corner_radius=8,
            font=("Arial", 12, "bold"),
            command=self._open_add_dialog,
        ).pack(side="right")

        table_card = ctk.CTkFrame(content, corner_radius=12, border_width=1, border_color="#3a3a4a")
        table_card.pack(fill="both", expand=True)

        header_row = ctk.CTkFrame(table_card, fg_color="#252540", corner_radius=8, height=38)
        header_row.pack(fill="x", padx=10, pady=(10, 4))

        ctk.CTkLabel(header_row, text="Status", font=("Arial", 12, "bold"), width=80).pack(side="left", padx=(16, 0))
        ctk.CTkLabel(header_row, text="Título", font=("Arial", 12, "bold"), width=200).pack(side="left", padx=12)
        ctk.CTkLabel(header_row, text="Descrição", font=("Arial", 12, "bold"), width=220).pack(side="left", padx=12)
        ctk.CTkLabel(header_row, text="Ações", font=("Arial", 12, "bold")).pack(side="right", padx=20)

        scrollable = ctk.CTkScrollableFrame(table_card, fg_color="transparent", corner_radius=0)
        scrollable.pack(fill="both", expand=True, padx=6, pady=(0, 6))

        if not tasks:
            ctk.CTkLabel(
                scrollable,
                text="Nenhuma tarefa cadastrada. Clique em '+ Adicionar Tarefa' para começar.",
                font=("Arial", 13),
                text_color="gray60",
            ).pack(pady=20)
            return

        done_count = sum(1 for t in tasks if t.get("done", False))
        ctk.CTkLabel(
            scrollable,
            text=f"{done_count}/{len(tasks)} tarefas concluídas",
            font=("Arial", 11),
            text_color="gray50",
        ).pack(anchor="e", padx=8, pady=(4, 2))

        for task in tasks:
            done = task.get("done", False)
            row = ctk.CTkFrame(scrollable, fg_color="#2b2b3b", corner_radius=6, height=44)
            row.pack(fill="x", pady=2)
            row.pack_propagate(False)

            status_color = "#27ae60" if done else "#e67e22"
            status_text = "Concluída" if done else "Pendente"

            status_lbl = ctk.CTkLabel(
                row,
                text=status_text,
                font=("Arial", 11, "bold"),
                text_color=status_color,
                width=80,
                anchor="w",
                cursor="hand2",
            )
            status_lbl.pack(side="left", padx=(16, 0))
            status_lbl.bind("<Button-1>", lambda e, t=task: self._open_detail_dialog(t))

            title_color = "gray55" if done else "white"
            title_lbl = ctk.CTkLabel(
                row,
                text=task["title"],
                font=("Arial", 12),
                text_color=title_color,
                width=200,
                anchor="w",
                cursor="hand2",
            )
            title_lbl.pack(side="left", padx=12)
            title_lbl.bind("<Button-1>", lambda e, t=task: self._open_detail_dialog(t))

            desc_lbl = ctk.CTkLabel(
                row,
                text=task.get("description", ""),
                font=("Arial", 11),
                text_color="gray60",
                width=220,
                anchor="w",
                cursor="hand2",
            )
            desc_lbl.pack(side="left", padx=12)
            desc_lbl.bind("<Button-1>", lambda e, t=task: self._open_detail_dialog(t))

            actions = ctk.CTkFrame(row, fg_color="transparent")
            actions.pack(side="right", padx=8)

            toggle_text = "Desfazer" if done else "Concluir"
            toggle_fg = "#7f8c8d" if done else "#27ae60"
            toggle_hover = "#95a5a6" if done else "#2ecc71"
            ctk.CTkButton(
                actions,
                text=toggle_text,
                width=82,
                height=28,
                corner_radius=6,
                fg_color=toggle_fg,
                hover_color=toggle_hover,
                font=("Arial", 11, "bold"),
                command=lambda tid=task["id"]: on_toggle(tid),
            ).pack(side="left", padx=3)

            ctk.CTkButton(
                actions,
                text="Editar",
                width=62,
                height=28,
                corner_radius=6,
                fg_color="#2980b9",
                hover_color="#3498db",
                font=("Arial", 11, "bold"),
                command=lambda t=task: self._open_edit_dialog(t),
            ).pack(side="left", padx=3)

            ctk.CTkButton(
                actions,
                text="Excluir",
                width=62,
                height=28,
                corner_radius=6,
                fg_color="#c0392b",
                hover_color="#e74c3c",
                font=("Arial", 11, "bold"),
                command=lambda tid=task["id"]: on_delete(tid),
            ).pack(side="left", padx=3)

    def _open_add_dialog(self):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Adicionar Tarefa")
        dialog.geometry("420x310")
        dialog.resizable(False, False)
        dialog.lift()
        dialog.focus_force()
        dialog.after(100, dialog.grab_set)

        ctk.CTkLabel(dialog, text="Nova Tarefa", font=("Arial", 16, "bold")).pack(pady=(24, 16))

        ctk.CTkLabel(dialog, text="Título *", font=("Arial", 13), anchor="w").pack(fill="x", padx=32, pady=(0, 4))
        title_entry = ctk.CTkEntry(dialog, width=340, height=38, placeholder_text="Título da tarefa", corner_radius=8)
        title_entry.pack(padx=32, pady=(0, 14))

        ctk.CTkLabel(dialog, text="Descrição", font=("Arial", 13), anchor="w").pack(fill="x", padx=32, pady=(0, 4))
        desc_entry = ctk.CTkEntry(dialog, width=340, height=38, placeholder_text="Descrição (opcional)", corner_radius=8)
        desc_entry.pack(padx=32, pady=(0, 24))

        ctk.CTkButton(
            dialog,
            text="Adicionar",
            width=340,
            height=42,
            corner_radius=8,
            font=("Arial", 13, "bold"),
            command=lambda: [self.on_add(title_entry.get(), desc_entry.get()), dialog.destroy()],
        ).pack(padx=32)

    def _open_edit_dialog(self, task):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Editar Tarefa")
        dialog.geometry("420x310")
        dialog.resizable(False, False)
        dialog.lift()
        dialog.focus_force()
        dialog.after(100, dialog.grab_set)

        ctk.CTkLabel(dialog, text="Editar Tarefa", font=("Arial", 16, "bold")).pack(pady=(24, 16))

        ctk.CTkLabel(dialog, text="Título *", font=("Arial", 13), anchor="w").pack(fill="x", padx=32, pady=(0, 4))
        title_entry = ctk.CTkEntry(dialog, width=340, height=38, corner_radius=8)
        title_entry.insert(0, task["title"])
        title_entry.pack(padx=32, pady=(0, 14))

        ctk.CTkLabel(dialog, text="Descrição", font=("Arial", 13), anchor="w").pack(fill="x", padx=32, pady=(0, 4))
        desc_entry = ctk.CTkEntry(dialog, width=340, height=38, corner_radius=8)
        desc_entry.insert(0, task.get("description", ""))
        desc_entry.pack(padx=32, pady=(0, 24))

        ctk.CTkButton(
            dialog,
            text="Salvar",
            width=340,
            height=42,
            corner_radius=8,
            font=("Arial", 13, "bold"),
            command=lambda: [self.on_edit(task["id"], title_entry.get(), desc_entry.get()), dialog.destroy()],
        ).pack(padx=32)

    def _open_detail_dialog(self, task):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Detalhes da Tarefa")
        dialog.geometry("480x380")
        dialog.resizable(False, False)
        dialog.lift()
        dialog.focus_force()
        dialog.after(100, dialog.grab_set)

        done = task.get("done", False)

        badge_color = "#27ae60" if done else "#e67e22"
        badge_text = "  Concluída  " if done else "  Pendente  "
        badge = ctk.CTkFrame(dialog, fg_color=badge_color, corner_radius=12, height=28)
        badge.pack(pady=(24, 0), padx=32, anchor="w")
        badge.pack_propagate(False)
        ctk.CTkLabel(badge, text=badge_text, font=("Arial", 11, "bold"), text_color="white").pack(expand=True)

        ctk.CTkLabel(
            dialog,
            text=task["title"],
            font=("Arial", 18, "bold"),
            anchor="w",
            wraplength=420,
        ).pack(fill="x", padx=32, pady=(12, 4))

        ctk.CTkFrame(dialog, height=1, fg_color="#3a3a4a").pack(fill="x", padx=32, pady=(0, 12))

        desc_text = task.get("description", "") or "Sem descrição."
        ctk.CTkLabel(
            dialog,
            text="Descrição",
            font=("Arial", 12, "bold"),
            text_color="gray60",
            anchor="w",
        ).pack(fill="x", padx=32, pady=(0, 4))
        ctk.CTkLabel(
            dialog,
            text=desc_text,
            font=("Arial", 13),
            anchor="nw",
            wraplength=420,
            justify="left",
        ).pack(fill="x", padx=32, pady=(0, 24))

        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(fill="x", padx=32, pady=(0, 24))

        toggle_text = "Desfazer Conclusão" if done else "Marcar como Concluída"
        toggle_fg = "#7f8c8d" if done else "#27ae60"
        toggle_hover = "#95a5a6" if done else "#2ecc71"

        ctk.CTkButton(
            btn_frame,
            text=toggle_text,
            height=42,
            corner_radius=8,
            fg_color=toggle_fg,
            hover_color=toggle_hover,
            font=("Arial", 13, "bold"),
            command=lambda: [self.on_toggle(task["id"]), dialog.destroy()],
        ).pack(fill="x", pady=(0, 8))

        ctk.CTkButton(
            btn_frame,
            text="Fechar",
            height=36,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#2b2b3b",
            border_width=1,
            border_color="#3a3a4a",
            font=("Arial", 12),
            command=dialog.destroy,
        ).pack(fill="x")

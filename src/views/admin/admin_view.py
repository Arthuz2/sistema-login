import customtkinter as ctk

class AdminView:
    def __init__(self, root, users, on_logout, on_delete, on_view_tasks):
        header = ctk.CTkFrame(root, height=56, corner_radius=0, fg_color="#1a2035")
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="Sistema de Tarefas - Painel Admin",
            font=("Arial", 15, "bold"),
            text_color="gray70",
        ).pack(side="left", padx=24)

        header_right = ctk.CTkFrame(header, height=56, corner_radius=0, fg_color="transparent")
        header_right.pack(side="right")

        ctk.CTkLabel(
            header_right,
            text="Painel Administrativo",
            font=("Arial", 13),
            text_color="#f39c12",
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

        ctk.CTkLabel(
            content,
            text="Gerenciamento de Usuários",
            font=("Arial", 17, "bold"),
        ).pack(fill="x", pady=(0, 14))

        table_card = ctk.CTkFrame(content, corner_radius=12, border_width=1, border_color="#3a3a4a")
        table_card.pack(fill="both", expand=True)

        header_row = ctk.CTkFrame(table_card, fg_color="#252540", corner_radius=8, height=38)
        header_row.pack(fill="x", padx=10, pady=(10, 4))

        ctk.CTkLabel(header_row, text="ID", font=("Arial", 12, "bold"), width=60).pack(side="left", padx=(16, 0))
        ctk.CTkLabel(header_row, text="Usuário", font=("Arial", 12, "bold"), width=220).pack(side="left", padx=12)
        ctk.CTkLabel(header_row, text="Ações", font=("Arial", 12, "bold")).pack(side="right", padx=20)

        scrollable = ctk.CTkScrollableFrame(table_card, fg_color="transparent", corner_radius=0)
        scrollable.pack(fill="both", expand=True, padx=6, pady=(0, 6))

        regular_users = [u for u in users if u["username"] != "admin"]

        if not regular_users:
            ctk.CTkLabel(
                scrollable,
                text="Nenhum usuário cadastrado.",
                font=("Arial", 13),
                text_color="gray60",
            ).pack(pady=20)
            return

        ctk.CTkLabel(
            scrollable,
            text=f"{len(regular_users)} usuário(s) cadastrado(s)",
            font=("Arial", 11),
            text_color="gray50",
        ).pack(anchor="e", padx=8, pady=(4, 2))

        for user in regular_users:
            row = ctk.CTkFrame(scrollable, fg_color="#2b2b3b", corner_radius=6, height=44)
            row.pack(fill="x", pady=2)
            row.pack_propagate(False)

            ctk.CTkLabel(
                row,
                text=str(user["id"]),
                font=("Arial", 12),
                width=60,
                anchor="w",
            ).pack(side="left", padx=(16, 0))

            ctk.CTkLabel(
                row,
                text=user["username"],
                font=("Arial", 12),
                width=220,
                anchor="w",
            ).pack(side="left", padx=12)

            actions = ctk.CTkFrame(row, fg_color="transparent")
            actions.pack(side="right", padx=8)

            ctk.CTkButton(
                actions,
                text="Ver Tarefas",
                width=100,
                height=28,
                corner_radius=6,
                fg_color="#2980b9",
                hover_color="#3498db",
                font=("Arial", 11, "bold"),
                command=lambda u=user: on_view_tasks(u["id"], u["username"]),
            ).pack(side="left", padx=3)

            ctk.CTkButton(
                actions,
                text="Excluir",
                width=70,
                height=28,
                corner_radius=6,
                fg_color="#c0392b",
                hover_color="#e74c3c",
                font=("Arial", 11, "bold"),
                command=lambda u=user: on_delete(u["id"], u["username"]),
            ).pack(side="left", padx=3)

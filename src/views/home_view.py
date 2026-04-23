import customtkinter as ctk

class HomeView:
    def __init__(self, root, username, on_logout, users=None):
        header = ctk.CTkFrame(root, height=56, corner_radius=0, fg_color="#1a2035")
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="Sistema de Login",
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

        if users:
            return self.list_user_table(content, users)
    
        self.greeting(content, username)

    def greeting(self, parent, username):
        card = ctk.CTkFrame(
            parent, corner_radius=14, border_width=1, border_color="#3a3a4a"
        )
        card.pack(expand=True)

        ctk.CTkLabel(
            card,
            text="Bem-vindo!",
            font=("Arial", 22, "bold"),
        ).pack(padx=52, pady=(40, 8))

        ctk.CTkLabel(
            card,
            text=f"Você está logado como  {username}.",
            font=("Arial", 13),
            text_color="gray60",
        ).pack(padx=52, pady=(0, 40))

    def list_user_table(self, parent, users):
        ctk.CTkLabel(
            parent,
            text="Usuários Cadastrados",
            font=("Arial", 17, "bold"),
        ).pack(fill="x", pady=(0, 14))

        table_card = ctk.CTkFrame(
            parent, corner_radius=12, border_width=1, border_color="#3a3a4a"
        )
        table_card.pack(fill="both", expand=True)

        header_row = ctk.CTkFrame(
            table_card, fg_color="#252540", corner_radius=8, height=38
        )
        header_row.pack(fill="x", padx=10, pady=(10, 4))

        ctk.CTkLabel(
            header_row,
            text="ID",
            font=("Arial", 12, "bold"),
            width=60,
        ).pack(side="left", padx=(16, 0))

        ctk.CTkLabel(
            header_row,
            text="Usuário",
            font=("Arial", 12, "bold"),
            width=220,
        ).pack(side="left", padx=12)

        scrollable = ctk.CTkScrollableFrame(
            table_card, fg_color="transparent", corner_radius=0
        )
        scrollable.pack(fill="both", expand=True, padx=6, pady=(0, 6))

        usersWithoutAdmin = list(filter(lambda user: user["username"] != "admin", users))
          
        if not usersWithoutAdmin:
          ctk.CTkLabel(
            scrollable,
            text="Nenhum usuário cadastrado.",
            font=("Arial", 13),
            text_color="gray60",
          ).pack(pady=20)
          return

        for user in usersWithoutAdmin:
          row = ctk.CTkFrame(
            scrollable, fg_color="#2b2b3b", corner_radius=6, height=36
          )
          row.pack(fill="x", pady=2)

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

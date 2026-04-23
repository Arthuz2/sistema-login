import customtkinter as ctk


class RegisterView:
    def __init__(self, root, on_register, on_back):
        main = ctk.CTkFrame(root, fg_color="transparent")
        main.pack(expand=True)

        ctk.CTkLabel(
            main,
            text="Criar Conta",
            font=("Arial", 26, "bold"),
        ).pack(pady=(0, 4))

        ctk.CTkLabel(
            main,
            text="Preencha os dados para se registrar",
            font=("Arial", 12),
            text_color="gray60",
        ).pack(pady=(0, 24))

        card = ctk.CTkFrame(
            main, corner_radius=14, border_width=1, border_color="#3a3a4a"
        )
        card.pack(padx=20)

        ctk.CTkLabel(
            card, text="Usuário", font=("Arial", 13), anchor="w"
        ).pack(fill="x", padx=32, pady=(28, 4))

        self.username_entry = ctk.CTkEntry(
            card,
            width=290,
            height=40,
            placeholder_text="Escolha um usuário",
            corner_radius=8,
        )
        self.username_entry.pack(padx=32, pady=(0, 18))

        ctk.CTkLabel(
            card, text="Senha", font=("Arial", 13), anchor="w"
        ).pack(fill="x", padx=32, pady=(0, 4))

        self.password_entry = ctk.CTkEntry(
            card,
            width=290,
            height=40,
            show="*",
            placeholder_text="Escolha uma senha",
            corner_radius=8,
        )
        self.password_entry.pack(padx=32, pady=(0, 24))

        ctk.CTkButton(
            card,
            text="Registrar",
            width=290,
            height=44,
            corner_radius=8,
            font=("Arial", 14, "bold"),
            command=lambda: on_register(
                self.username_entry.get(), self.password_entry.get()
            ),
        ).pack(padx=32, pady=(0, 28))

        footer = ctk.CTkFrame(main, fg_color="transparent")
        footer.pack(pady=(18, 0))

        ctk.CTkLabel(
            footer, text="Já tem uma conta?", font=("Arial", 12)
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            footer,
            text="Entrar",
            font=("Arial", 12, "bold"),
            fg_color="transparent",
            hover_color="#2b2b3b",
            text_color="#4da8da",
            width=60,
            height=28,
            command=on_back,
        ).pack(side="left")

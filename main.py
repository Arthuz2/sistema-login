import customtkinter as ctk
from src.controllers.login_controller import LoginController

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class CTk(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("800x600")
        LoginController(self).login_view()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    end = CTk()
    end.mainloop()
import tkinter as tk
from tkinter import messagebox
from client import Client
import time

class LoginGUI:
    def __init__(self):
        self.client = Client()
        self.root = tk.Tk()
        self.root.title("FUTRADE - Login / Sign Up")
        self.root.geometry("480x520")
        self.root.configure(bg="#0b0c10")
        self.root.resizable(False, False)
        self.mode = "login"  # login או signup
        self.show_password = False
        self.root.attributes("-alpha", 0.0)  # מתחיל שקוף
        self.create_widgets()
        self.fade_in()  # ✨ מפעיל את האנימציה
        self.root.mainloop()

    def fade_in(self):
        """אנימציית כניסה הדרגתית"""
        for i in range(0, 101, 5):
            self.root.attributes("-alpha", i / 100)
            self.root.update()
            time.sleep(0.02)

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="LOGIN", font=("Arial", 28, "bold"), fg="#00ff7f", bg="#0b0c10")
        self.title_label.pack(pady=40)

        # שם משתמש
        tk.Label(self.root, text="Username", fg="lightgray", bg="#0b0c10", font=("Arial", 12)).pack()
        self.username_entry = tk.Entry(self.root, bg="#1f2833", fg="white", font=("Arial", 12),
                                       relief="flat", width=28, insertbackground="white")
        self.username_entry.pack(pady=10, ipady=4)

        # סיסמה
        tk.Label(self.root, text="Password", fg="lightgray", bg="#0b0c10", font=("Arial", 12)).pack()
        self.password_entry = tk.Entry(self.root, show="*", bg="#1f2833", fg="white", font=("Arial", 12),
                                       relief="flat", width=28, insertbackground="white")
        self.password_entry.pack(pady=10, ipady=4)

        # כפתור הצגת סיסמה
        self.show_pass_btn = tk.Button(self.root, text="👁 Show Password", font=("Arial", 10),
                                       bg="#1f2833", fg="#00ff7f", relief="flat",
                                       command=self.toggle_password)
        self.show_pass_btn.pack(pady=10)

        # כפתור פעולה (Login / Sign up)
        self.action_btn = tk.Button(self.root, text="🚀 LOGIN", font=("Arial", 14, "bold"),
                                    bg="#1f2833", fg="#00ff7f", relief="flat", width=20, height=2,
                                    activebackground="#45a29e", command=self.login_or_signup)
        self.action_btn.pack(pady=25)

        # 🟩 מסגרת תחתונה עם ה-SignUp וה-footer ביחד
        bottom_frame = tk.Frame(self.root, bg="#0b0c10")
        bottom_frame.pack(side="bottom", pady=20)

        self.switch_label = tk.Label(bottom_frame, text="Don't have an account?", fg="lightgray", bg="#0b0c10")
        self.switch_label.pack()

        self.switch_btn = tk.Button(bottom_frame, text="Sign Up", font=("Arial", 10, "underline"),
                                    fg="#00ff7f", bg="#0b0c10", relief="flat", command=self.switch_mode)
        self.switch_btn.pack(pady=2)

        footer = tk.Label(bottom_frame, text="© 2025 FUTRADE Project", font=("Arial", 9),
                          fg="#c5c6c7", bg="#0b0c10")
        footer.pack(pady=(8, 0))

    def toggle_password(self):
        """הצגה/הסתרת הסיסמה"""
        if self.show_password:
            self.password_entry.config(show="*")
            self.show_pass_btn.config(text="👁 Show Password")
        else:
            self.password_entry.config(show="")
            self.show_pass_btn.config(text="🙈 Hide Password")
        self.show_password = not self.show_password

    def switch_mode(self):
        """מעבר בין Login ל־Sign Up"""
        if self.mode == "login":
            self.mode = "signup"
            self.title_label.config(text="SIGN UP")
            self.action_btn.config(text="📝 SIGN UP")
            self.switch_label.config(text="Already have an account?")
            self.switch_btn.config(text="Login")
        else:
            self.mode = "login"
            self.title_label.config(text="LOGIN")
            self.action_btn.config(text="🚀 LOGIN")
            self.switch_label.config(text="Don't have an account?")
            self.switch_btn.config(text="Sign Up")

    def login_or_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return

        if self.mode == "login":
            response = self.client.login(username, password)
            if response == "LOGIN_SUCCESS":
                messagebox.showinfo("Success", f"Welcome {username}!")
            else:
                messagebox.showerror("Failed", "Incorrect username or password")
        else:
            response = self.client.signup(username, password)
            if response == "SIGNUP_SUCCESS":
                messagebox.showinfo("Success", "Account created successfully! You can now login.")
                self.switch_mode()
            else:
                messagebox.showerror("Failed", "Username already exists!")

if __name__ == "__main__":
    LoginGUI()

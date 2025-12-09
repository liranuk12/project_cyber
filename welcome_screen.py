import tkinter as tk
import time
from gui import LoginGUI

class WelcomeScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FUTRADE")
        self.root.geometry("500x420")
        self.root.configure(bg="#0b0c10")
        self.root.resizable(False, False)

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # כותרת ראשית / לוגו
        title = tk.Label(
            self.root,
            text="FUTRADE",
            font=("Arial", 36, "bold"),
            fg="#00ff7f",
            bg="#0b0c10"
        )
        title.pack(pady=80)

        # תת-כותרת / תיאור קצר
        subtitle = tk.Label(
            self.root,
            text="Build your dream team and trade players with friends",
            font=("Arial", 12),
            fg="lightgray",
            bg="#0b0c10"
        )
        subtitle.pack(pady=10)

        # כפתור כניסה
        enter_button = tk.Button(
            self.root,
            text="🚀 Enter FUTRADE",
            font=("Arial", 14, "bold"),
            bg="#1f2833",
            fg="#00ff7f",
            relief="flat",
            width=18,
            height=2,
            activebackground="#45a29e",
            command=self.fade_out_and_open_login
        )
        enter_button.pack(pady=50)

        # טקסט תחתון
        footer = tk.Label(
            self.root,
            text="© 2025 FUTRADE Project",
            font=("Arial", 9),
            fg="#c5c6c7",
            bg="#0b0c10"
        )
        footer.pack(side="bottom", pady=10)

    def fade_out_and_open_login(self):
        """מעבר הדרגתי לפני פתיחת מסך ההתחברות"""
        for i in range(100, -1, -5):
            self.root.attributes("-alpha", i / 100)
            self.root.update()
            time.sleep(0.02)
        self.root.destroy()
        LoginGUI()

if __name__ == "__main__":
    WelcomeScreen()

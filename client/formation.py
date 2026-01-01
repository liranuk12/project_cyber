import tkinter as tk
from PIL import Image, ImageTk  # חייב pillow מותקן
# pip install pillow
class FormationGUI:
    def __init__(self, username):
        self.root = tk.Toplevel()     # <<< FIXED - no new Tk()
        self.root.title("Team Formation")
        self.root.geometry("600x800")
        self.root.configure(bg="#0b0c10")
        self.root.resizable(False, False)


        tk.Label(self.root, text="⚽ 4-3-3 Team Layout",
                 font=("Arial", 26, "bold"), fg="#00ff7f", bg="#0b0c10").pack(pady=20)

        # Load images pic1.jpg ... pic11.jpg
        self.images = []
        for i in range(1, 12):
            img = Image.open(f"players_pics/bellingham.jpg").resize((90, 90))
            self.images.append(ImageTk.PhotoImage(img))

        field = tk.Frame(self.root, bg="#0b0c10")
        field.pack(pady=30)

        # ============= התקפה 3 שחקנים (Top) ============
        row_attack = tk.Frame(field, bg="#0b0c10")
        row_attack.grid(row=0, column=0, pady=25)
        for idx in range(8, 11):   # players 9,10,11
            self.create_player_btn(row_attack, idx)

        # ============= קישור 3 שחקנים ============
        row_mid = tk.Frame(field, bg="#0b0c10")
        row_mid.grid(row=1, column=0, pady=25)
        for idx in range(5, 8):    # players 6,7,8
            self.create_player_btn(row_mid, idx)

        # ============= הגנה 4 שחקנים ============
        row_def = tk.Frame(field, bg="#0b0c10")
        row_def.grid(row=2, column=0, pady=25)
        for idx in range(1, 5):    # players 2,3,4,5
            self.create_player_btn(row_def, idx)

        # ============= שוער (Bottom) ============
        row_gk = tk.Frame(field, bg="#0b0c10")
        row_gk.grid(row=3, column=0, pady=25)
        self.create_player_btn(row_gk, 0, colspan=4)  # player 1 (GK) centered

        tk.Label(self.root, text="© 2025 FUTRADE",
                 fg="#c5c6c7", bg="#0b0c10", font=("Arial", 10)).pack(side="bottom", pady=10)

        self.root.mainloop()

    def create_player_btn(self, parent, idx, colspan=1):
        btn = tk.Button(parent,
                        image=self.images[idx],
                        bg="#1f2833", relief="flat",
                        activebackground="#45a29e",
                        command=lambda i=idx: self.open_all_players(i))

        if colspan > 1:
            btn.grid(row=0, column=0, columnspan=colspan, pady=10)
        else:
            btn.grid(row=0, column=idx, padx=15)

    def open_all_players(self, player_index):
        print(f"Player #{player_index+1} clicked")
        # here later you'll call AllPlayers screen
        # AllPlayersGUI(player_index)


# f = FormationGUI("fd")
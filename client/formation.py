import tkinter as tk
from PIL import Image, ImageTk  # חייב pillow מותקן
# pip install pillow


class FormationGUI:
    def __init__(self, client, user_id):
        self.client = client
        self.user_id = user_id
        self.root = tk.Toplevel()     # <<< FIXED - no new Tk()
        self.root.title("Team Formation")
        self.root.geometry("600x800")
        self.root.configure(bg="#0b0c10")
        self.root.resizable(False, False)
        field = tk.Frame(self.root, bg="#0b0c10")
        field.pack(pady=30)

        # ===== התקפה =====
        row_attack = tk.Frame(field, bg="#0b0c10")
        row_attack.grid(row=0, column=0, pady=25)

        # ===== קישור =====
        row_mid = tk.Frame(field, bg="#0b0c10")
        row_mid.grid(row=1, column=0, pady=25)

        # ===== הגנה =====
        row_def = tk.Frame(field, bg="#0b0c10")
        row_def.grid(row=2, column=0, pady=25)

        # ===== שוער =====
        row_gk = tk.Frame(field, bg="#0b0c10")
        row_gk.grid(row=3, column=0, pady=25)

        self.load_team()
        
        formation = self.split_by_position()

        # התקפה
        for p in formation["ATT"][:3]:
            self.create_player_btn(row_attack, p)

        # קישור
        for p in formation["MID"][:3]:
            self.create_player_btn(row_mid, p)

        # הגנה
        for p in formation["DEF"][:4]:
            self.create_player_btn(row_def, p)

        # שוער
        if formation["GK"]:
            self.create_player_btn(row_gk, formation["GK"][0])

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

    def create_player_btn(self, parent, player):
        img = self.load_player_image(player["id"])

        btn = tk.Button(
            parent,
            image=img,
            bg="#1f2833",
            relief="flat",
            activebackground="#45a29e",
            command=lambda p=player: self.on_player_click(p)
        )

        btn.image = img  # חשוב – אחרת התמונה נעלמת
        btn.pack(side="left", padx=15)

    def load_team(self):
        """
        מבקש מהשרת את כל השחקנים של המשתמש
        """
        self.team_players = self.client.get_my_team(self.user_id)

    def split_by_position(self):
        formation = {
            "GK": [],
            "DEF": [],
            "MID": [],
            "ATT": []
        }

        formation_position = { "GK": [ "GK"], "DEF": ["CB","LB","RB"],"MID": ["CDM","CAM","CM"],
            "ATT": ["RW","LW","ST"]}
        for p in self.team_players:
            pos = p["position"]

            for group, positions in formation_position.items():
                if pos in positions:
                    formation[group].append(p)
                    break

        return formation

    def load_player_image(self, player_id):
        img = self.client.get_player_image(player_id)
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)

    def on_player_click(self, player):
        print("Selected:", player["first_name"], player["last_name"])
        # בהמשך:
        # open market to replace
        # sell player

    def open_all_players(self, position_index):
        from market_gui import MarketGUI
        MarketGUI(self.client, self.user_id)
        # here later you'll call AllPlayers screen
        # AllPlayersGUI(player_index)


# f = FormationGUI("fd")
import tkinter as tk
from PIL import Image, ImageTk

from change_formation_popup import ChangeFormationPopup


class FormationGUI:
    def __init__(self, client, user_id):
        self.client = client
        self.user_id = user_id

        self.root = tk.Toplevel()
        self.root.title("Team Formation")
        self.root.configure(bg="#0b0c10")
        self.root.resizable(False, False)

        # ===== התאמה לגודל המסך =====
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()

        w = int(screen_w *0.85)
        h = int(screen_h* 0.85)
        self.root.geometry(f"{w}x{h}+50+50")

        # scale יחסי למסך 1080p
        self.scale = (screen_h / 1080)/1.2

        # ===== כותרת =====
        tk.Label(
            self.root,
            text="⚽ 4-3-3 Team Layout",
            font=("Arial", int(26 * self.scale), "bold"),
            fg="#00ff7f",
            bg="#0b0c10"
        ).pack(pady=int(15 * self.scale))

        # ===== מגרש =====
        field = tk.Frame(self.root, bg="#0b0c10")
        field.pack(pady=int(20 * self.scale))

        pad_y = int(25 * self.scale)

        row_attack = tk.Frame(field, bg="#0b0c10")
        row_attack.grid(row=0, column=0, pady=pad_y)

        row_mid = tk.Frame(field, bg="#0b0c10")
        row_mid.grid(row=1, column=0, pady=pad_y)

        row_def = tk.Frame(field, bg="#0b0c10")
        row_def.grid(row=2, column=0, pady=pad_y)

        row_gk = tk.Frame(field, bg="#0b0c10")
        row_gk.grid(row=3, column=0, pady=pad_y)

        # ===== טעינת שחקנים =====
        self.load_team()
        formation = self.split_by_position()

        for p in formation["ATT"][:3]:
            self.create_player_btn(row_attack, p)

        for p in formation["MID"][:3]:
            self.create_player_btn(row_mid, p)

        for p in formation["DEF"][:4]:
            self.create_player_btn(row_def, p)

        if formation["GK"]:
            self.create_player_btn(row_gk, formation["GK"][0])

        # ===== Footer =====
        tk.Label(
            self.root,
            text="© 2025 FUTRADE",
            fg="#c5c6c7",
            bg="#0b0c10",
            font=("Arial", int(10 * self.scale))
        ).pack(side="bottom", pady=int(10 * self.scale))

    # ================= UI =================

    def create_player_btn(self, parent, player):
        player_frame = tk.Frame(parent, bg="#0b0c10")

        img = self.load_player_image(player["id"])


        atk = player["attack"]
        dfns = player["defense"]
        psn = player["possession"]

        btn = tk.Button(
            player_frame,
            image=img,
            bg="#1f2833",
            relief="flat",
            activebackground="#45a29e",
            command=lambda p=player: self.on_player_click(p)
        )

        stats = tk.Label(player_frame,text=f"{atk} {dfns} {psn}", fg="#ffffff", bg="#000000")

        btn.image = img  # חובה לשמור רפרנס
        btn.pack(side="top", padx=int(15 * self.scale))
        stats.pack(side="bottom")
        player_frame.pack(side="right")

    # ================= DATA =================

    def load_team(self):
        self.team_players = self.client.get_my_team(self.user_id)

    def split_by_position(self):
        formation = {
            "GK": [],
            "DEF": [],
            "MID": [],
            "ATT": []
        }

        formation_position = {
            "GK": ["GK"],
            "DEF": ["CB", "LB", "RB"],
            "MID": ["CDM", "CAM", "CM"],
            "ATT": ["RW", "LW", "ST"]
        }

        for p in self.team_players:
            pos = p["position"]
            for group, positions in formation_position.items():
                if pos in positions:
                    formation[group].append(p)
                    break

        return formation

    def load_player_image(self, player_id):
        base_size = 150
        size = int(base_size * self.scale)

        img = self.client.get_player_image(player_id)
        img = img.resize((size, size))
        return ImageTk.PhotoImage(img)

    # ================= ACTION =================

    def on_player_click(self, player):
        print("Selected:", player["first_name"], player["last_name"])

        dialog = ChangeFormationPopup(self.root,self.client,self.user_id,player)
        self.root.wait_window(dialog.root)
        # בהמשך:
        # החלפה / מכירה / פתיחת Market

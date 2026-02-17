import tkinter as tk
from PIL import Image, ImageTk

from change_formation_popup import ChangeFormationPopup


class FormationGUI:
    FORMATION_POSITION = {
        "GK": ["GK"],
        "DEF": ["RB","RCB", "LCB","LB" ],
        "MID": ["CDM", "CAM", "CM"],
        "ATT": ["RW", "ST","LW"]
    }
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

        w = int(screen_w * 0.85)
        h = int(screen_h * 0.85)
        self.root.geometry(f"{w}x{h}+50+50")

        # scale יחסי למסך 1080p
        self.scale = (screen_h / 1080) / 1.2

        # ===== כותרת =====
        tk.Label(
            self.root,
            text="⚽ 4-3-3 Team Layout",
            font=("Arial", int(26 * self.scale), "bold"),
            fg="#00ff7f",
            bg="#0b0c10"
        ).pack(pady=int(15 * self.scale))
        self.field = tk.Frame(self.root, bg="#0b0c10")
        self.field.pack(pady=int(20 * self.scale))
        self.create_formation()


    def create_formation(self):
        # ===== מגרש =====

        pad_y = int(25 * self.scale)

        row_attack = tk.Frame(self.field, bg="#0b0c10")
        row_attack.grid(row=0, column=0, pady=pad_y)

        row_mid = tk.Frame(self.field, bg="#0b0c10")
        row_mid.grid(row=1, column=0, pady=pad_y)

        row_def = tk.Frame(self.field, bg="#0b0c10")
        row_def.grid(row=2, column=0, pady=pad_y)

        row_gk = tk.Frame(self.field, bg="#0b0c10")
        row_gk.grid(row=3, column=0, pady=pad_y)

        # ===== טעינת שחקנים =====
        self.load_team()
        print(self.team_players)
        formation = self.split_by_position()
        print(formation)

        for i, p in enumerate(formation["ATT"][:3]):
            self.create_player_btn(row_attack, p, self.FORMATION_POSITION["ATT"][i])

        for i, p in enumerate(formation["MID"][:3]):
            self.create_player_btn(row_mid, p, self.FORMATION_POSITION["MID"][i])

        for i, p in enumerate(formation["DEF"][:4]):
            self.create_player_btn(row_def, p, self.FORMATION_POSITION["DEF"][i])

        if formation["GK"]:
            self.create_player_btn(row_gk, formation["GK"][0], "GK")

        # ===== Footer =====
        tk.Label(
            self.root,
            text="© 2025 FUTRADE",
            fg="#c5c6c7",
            bg="#0b0c10",
            font=("Arial", int(10 * self.scale))
        ).pack(side="bottom", pady=int(10 * self.scale))
    # ================= UI =================

    def create_player_btn(self, parent, player, position):
        player_frame = tk.Frame(parent, bg="#0b0c10")

        if player:
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
                command=lambda : self.on_player_click(position,player)
            )

            stats = tk.Label(player_frame, text=f"{atk} {dfns} {psn}", fg="#ffffff", bg="#000000")

            btn.image = img  # חובה לשמור רפרנס

            stats.pack(side="bottom")

        else:
            btn = tk.Button(
                player_frame,
                width=20,
                height=10,
                command=lambda : self.on_player_click(position,player),
                relief="flat",
                activebackground="#45a29e",
            )
        btn.pack(
            side="left",
            padx=int(15*self.scale),
             )
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

        found_player_for_position = False
        for group,positions in self.FORMATION_POSITION.items():
            for position in positions:
                found_player_for_position = False
                for player in self.team_players:
                    if player["position"] == position and player["is_field_player"]:
                        found_player_for_position = True
                        formation[group].append(player)
                        break
                if found_player_for_position is False:
                    formation[group].append(None)


        # for p in self.team_players:
        #     pos = p["position"]
        #     is_in_field = p["is_field_player"]
        #     for group, positions in formation_position.items():
        #         if pos in positions and is_in_field:
        #             formation[group].append(p)
        #             break

        return formation

    def load_player_image(self, player_id):
        base_size = 150
        size = int(base_size * self.scale)

        img = self.client.get_player_image(player_id)
        img = img.resize((size, size))
        return ImageTk.PhotoImage(img)

    # ================= ACTION =================

    def on_player_click(self, position,player):
        if player:
            dialog = ChangeFormationPopup(self.root, self.client, self.user_id, position,self.team_players,player["id"])
        else:
            dialog = ChangeFormationPopup(self.root, self.client, self.user_id, position, self.team_players,
                                          None)
        self.root.wait_window(dialog.root)
        self.refresh_formation()

        # בהמשך:
        # החלפה / מכירה / פתיחת Market


    def refresh_formation(self):
        for child in self.field.winfo_children():
            child.destroy()
        self.create_formation()

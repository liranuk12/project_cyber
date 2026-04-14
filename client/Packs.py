import tkinter as tk
import json
from PIL import Image, ImageTk


BG_MAIN = "#0b0c10"
BG_CARD = "#1f2833"
FG_PRIMARY = "#00ff7f"
FG_TEXT = "#c5c6c7"
FG_LIGHT = "lightgray"
ACTIVE_BG = "#45a29e"


class PacksScreen(tk.Toplevel):
    def __init__(self, client, username):
        super().__init__()
        self.client = client
        self.username = username

        self.configure(bg=BG_MAIN)
        self.title("Packs")
        self.geometry("700x700")
        self.resizable(False, False)

        title_label = tk.Label(
            self,
            text="PACKS",
            font=("Arial", 26, "bold"),
            fg=FG_PRIMARY,
            bg=BG_MAIN
        )
        title_label.pack(pady=20)

        frame = tk.Frame(self, bg=BG_MAIN)
        frame.pack(pady=10)

        packs = json.load(open("Assets/Strings/packs.json", "r", encoding="utf-8"))
        for pack, pack_content in packs.items():
            pack_name = pack_content["name"]
            pack_description = pack_content["description"]
            pack_image = pack_content["image"]
            pack_requirement = pack_content["requirement"]

            Pack(
                frame,
                pack_name,
                pack_description,
                pack_image,
                client,
                pack_requirement,
                username
            )


class Pack(tk.Frame):
    def __init__(self, parent, pack_name, pack_description, pack_img, client, pack_requirement, username):
        super().__init__(
            parent,
            bg=BG_CARD,
            bd=0,
            highlightthickness=1,
            highlightbackground=FG_PRIMARY,
            padx=15,
            pady=15
        )

        self.pack_requirement = pack_requirement
        self.pack_name = pack_name
        self.pack_description = pack_description
        self.client = client
        self.username = username

        img = Image.open(f"Assets/images{pack_img}")
        img = img.resize((120, 120))
        self.img = ImageTk.PhotoImage(img)

        img_label = tk.Label(self, image=self.img, bg=BG_CARD)
        img_label.pack(side="left", padx=(0, 15))

        pack_content = tk.Frame(self, bg=BG_CARD)
        pack_content.pack(side="left", fill="both", expand=True)

        name_label = tk.Label(
            pack_content,
            text=pack_name,
            font=("Arial", 16, "bold"),
            fg=FG_PRIMARY,
            bg=BG_CARD
        )
        name_label.pack(anchor="w", pady=(5, 8))

        description_label = tk.Label(
            pack_content,
            text=pack_description,
            font=("Arial", 11),
            fg=FG_TEXT,
            bg=BG_CARD,
            wraplength=350,
            justify="left"
        )
        description_label.pack(anchor="w", pady=(0, 12))



        open_pack_btn = tk.Button(
            pack_content,
            text="OPEN",
            font=("Arial", 12, "bold"),
            bg=BG_CARD,
            fg=FG_PRIMARY,
            relief="flat",
            width=14,
            height=1,
            activebackground=ACTIVE_BG,
            activeforeground="white",
            command=self.handle_open_pack
        )
        open_pack_btn.pack(anchor="w")

        self.pack(fill="x", padx=20, pady=12)

    def handle_open_pack(self):
        print(f"opening pack {self.pack_name}")

        response = self.client.open_pack(self.username, self.pack_requirement)
        if response is not False:
            new_player_id = response
            player_img = self.client.get_player_image(new_player_id)
            player_img = player_img.resize((140, 140))
            player_name = self.client.get_player_name(new_player_id)
            PlayerDetails(player_name, ImageTk.PhotoImage(player_img))


class PlayerDetails(tk.Toplevel):
    def __init__(self, player_name, player_img):
        super().__init__()
        self.title("New Player")
        self.geometry("500x450")
        self.configure(bg=BG_MAIN)
        self.resizable(False, False)

        self.player_img = player_img

        frame = tk.Frame(self, bg=BG_MAIN)
        frame.pack(expand=True)

        title_label = tk.Label(
            frame,
            text="PACK OPENED",
            font=("Arial", 22, "bold"),
            fg=FG_PRIMARY,
            bg=BG_MAIN
        )
        title_label.pack(pady=(20, 10))

        subtitle_label = tk.Label(
            frame,
            text="You got a new player!",
            font=("Arial", 12),
            fg=FG_TEXT,
            bg=BG_MAIN
        )
        subtitle_label.pack(pady=(0, 20))

        image_holder = tk.Label(
            frame,
            image=self.player_img,
            bg=BG_CARD,
            relief="flat",
            bd=0
        )
        image_holder.pack(pady=10, ipadx=15, ipady=15)

        name_label = tk.Label(
            frame,
            text=player_name,
            font=("Arial", 16, "bold"),
            fg=FG_PRIMARY,
            bg=BG_MAIN
        )
        name_label.pack(pady=15)

        close_btn = tk.Button(
            frame,
            text="CLOSE",
            font=("Arial", 12, "bold"),
            bg=BG_CARD,
            fg=FG_PRIMARY,
            relief="flat",
            width=14,
            height=1,
            activebackground=ACTIVE_BG,
            activeforeground="white",
            command=self.destroy
        )
        close_btn.pack(pady=20)
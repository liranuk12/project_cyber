import tkinter as tk
from PIL import Image, ImageTk


class ChangeFormationPopup:
    def __init__(self,parent, client, user_id,position,players,current_player_id):
        self.client = client
        self.user_id = user_id
        self.position = position
        self.players = players
        self.current_player_id = current_player_id

        self.root = tk.Toplevel()
        self.root.title("change formation popup")
        self.root.configure(bg="#0b0c10")
        self.root.geometry("600x600")

        # Direct all events to the dialog window (freezes the main window)
        self.root.grab_set()
        self.root.transient(parent)

        filtered_players = self.filter_field()

        self.list_frame = tk.Frame(self.root, bg="#0b0c10")
        self.list_frame.pack(fill="both", expand=True, pady=20)

        self.canvas = tk.Canvas(self.list_frame, bg="#0b0c10", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#0b0c10")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        for player in filtered_players:
            self.create_player_row(player,self.scrollable_frame)


    def filter_field(self):
        filtered_players = []
        for player in self.players:
            if not player["is_field_player"] and player["position"] == self.position:
                filtered_players.append(player)
        return filtered_players

    def create_player_row(self,player,parent):
        player_id = player["id"]
        first = player["first_name"]
        last = player["last_name"]
        position = player["position"]
        club = player["club"]

        row = tk.Frame(parent, bg="#1f2833", height=50)
        row.pack(fill="x", padx=40, pady=8)
        player_name_label = tk.Label(
            row,
            text=f"{first} {last}  |  {position}  |  {club}",
            font=("Arial", 14),
            fg="white",
            bg="#1f2833"
        )

        player_name_label.pack(side="left", padx=20)

        select_player_btn = tk.Button(
            row,
            text="Select",
            font=("Arial", 12, "bold"),
            bg="#0b0c10",
            fg="#00ff7f",
            relief="flat",
            width=8,
            command=lambda pid=player_id: self.add_player_to_formation(player_id)
        )
        select_player_btn.pack(side="left", padx=20)

    def add_player_to_formation(self,player_id):
        print(f"selected player: {player_id}")
        if self.current_player_id is not None:
            self.client.replace_player_in_formation(self.user_id,self.current_player_id,player_id)
        else:
            self.client.insert_player_in_formation(self.user_id,player_id)
        self.root.destroy()





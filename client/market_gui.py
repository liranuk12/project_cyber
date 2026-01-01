import tkinter as tk
from tkinter import messagebox


class MarketGUI:
    def __init__(self, client, user_id="a"):
        self.user_id = user_id
        self.client = client

        self.root = tk.Tk()
        self.root.title("FUTRADE - Transfer Market")
        self.root.geometry("900x600")
        self.root.configure(bg="#0b0c10")
        self.root.resizable(False, False)

        self.create_widgets()
        self.load_players_from_server()

        self.root.mainloop()

    # ================= UI =================

    def create_widgets(self):
        tk.Label(
            self.root,
            text="TRANSFER MARKET",
            font=("Arial", 26, "bold"),
            fg="#00ff7f",
            bg="#0b0c10"
        ).pack(pady=20)

        # ---- FILTER BAR ----
        filter_frame = tk.Frame(self.root, bg="#0b0c10")
        filter_frame.pack(pady=10)

        for text in ["NAME", "PRICE", "POSITION", "NATIONALITY", "LEAGUE"]:
            tk.Entry(
                filter_frame,
                width=12,
                bg="#1f2833",
                fg="white",
                relief="flat",
                justify="center",
                insertbackground="white"
            ).pack(side="left", padx=6, ipady=4)

        tk.Button(
            filter_frame,
            text="🔍",
            font=("Arial", 14),
            bg="#1f2833",
            fg="#00ff7f",
            relief="flat",
            width=4
        ).pack(side="left", padx=10)

        # ---- PLAYERS LIST ----
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

    # ================= DATA =================

    def load_players_from_server(self):
        players = self.client.get_missing_players(self.user_id)

        for player in players:
            self.add_player_row(player)

    def add_player_row(self, player):
        """
        player is dict:
        {
            id, first_name, last_name, position, club
        }
        """
        player_id = player["id"]
        first = player["first_name"]
        last = player["last_name"]
        position = player["position"]
        club = player["club"]

        row = tk.Frame(self.scrollable_frame, bg="#1f2833", height=50)
        row.pack(fill="x", padx=40, pady=8)

        tk.Label(
            row,
            text=f"{first} {last}  |  {position}  |  {club}",
            font=("Arial", 14),
            fg="white",
            bg="#1f2833"
        ).pack(side="left", padx=20)

        tk.Button(
            row,
            text="BUY",
            font=("Arial", 12, "bold"),
            bg="#0b0c10",
            fg="#00ff7f",
            relief="flat",
            width=8,
            command=lambda pid=player_id: self.buy_player(pid)
        ).pack(side="right", padx=20)

    # ================= ACTION =================

    def buy_player(self, player_id):
        response = self.client.buy_player(self.user_id, player_id)

        if response == "BUY_SUCCESS":
            messagebox.showinfo("Success", "Player purchased successfully!")

            # ניקוי הרשימה הקיימת
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # טעינה מחדש מהשרת
            self.load_players_from_server()

        else:
            messagebox.showerror("Error", "BUY FAILED\nPlayer already owned or error occurred.")

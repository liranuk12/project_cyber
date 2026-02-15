import tkinter as tk
from PIL import Image, ImageTk


class ChangeFormationPopup:
    def __init__(self,parent, client, user_id,original_player):
        self.client = client
        self.user_id = user_id
        self.original_player = original_player

        self.root = tk.Toplevel()
        self.root.title("change formation popup")
        self.root.configure(bg="#0b0c10")

        # Direct all events to the dialog window (freezes the main window)
        self.root.grab_set()
        self.root.transient(parent)




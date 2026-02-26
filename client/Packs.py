import tkinter as tk
import json

from PIL import Image,ImageTk


class PacksScreen(tk.Toplevel):
    def __init__(self, client, username):
        tk.Toplevel.__init__(self)
        self.client = client
        self.username = username
        self.title("Packs")
        self.geometry("700x700")
        frame = tk.Frame(self)

        packs = json.load(open("Assets/Strings/packs.json"))
        for pack,pack_content in packs.items():
            print(pack,pack_content)
            pack_name = pack_content["name"]
            pack_description = pack_content["description"]
            pack_image = pack_content["image"]
            pack_requirement = pack_content["requirement"]
            print(pack_name,pack_description,pack_image)
            futrade_pack = Pack(frame,pack_name, pack_description, pack_image,client,pack_requirement,username)

        frame.pack()




class Pack(tk.Frame):
    def __init__(self,parent, pack_name,pack_description,pack_img,client,pack_requirement,username):
        self.pack_requirement = pack_requirement
        tk.Frame.__init__(self,parent)
        self.pack_name = pack_name
        self.pack_description = pack_description
        self.client = client
        self.username = username
        img = Image.open(f"Assets/images{pack_img}")
        img = img.resize((120, 120))  # width, height
        self.img = ImageTk.PhotoImage(img)
        img_label = tk.Label(self, image=self.img)
        img_label.pack(side="left")

        pack_content = tk.Frame(self)
        name_label = tk.Label(pack_content, text=pack_name)
        description_label = tk.Label(pack_content, text=pack_description)
        open_pack_btn = tk.Button(pack_content, text="Open")

        pack_content.pack(side="right")
        name_label.pack(side="top")
        description_label.pack(side="bottom")
        open_pack_btn.pack(side="bottom")
        self.pack()

        open_pack_btn.configure(command=lambda :self.handle_open_pack())

    def handle_open_pack(self):
        print(f"opening pack {self.pack_name}")

        self.client.open_pack(self.username,self.pack_requirement)
        return







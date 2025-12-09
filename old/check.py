import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# -----------------------------
# פונקציה לטעינת תמונה מהאינטרנט
# -----------------------------
def load_image_from_url(url, size=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        if "image" not in response.headers.get("Content-Type", ""):
            print("URL לא מחזיר תמונה:", url)
            return None

        img_data = response.content
        img = Image.open(BytesIO(img_data))

        if size:
            img = img.resize(size)

        return ImageTk.PhotoImage(img)

    except Exception as e:
        print("שגיאה בטעינת התמונה:", e)
        return None

# -----------------------------
# הקוד שלך שמציג את התמונה
# -----------------------------
root = tk.Tk()
root.title("תצוגת תמונה")

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Lionel_Messi_20180626.jpg/440px-Lionel_Messi_20180626.jpg"

photo = load_image_from_url(url, size=(200, 200))

if photo:
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
else:
    tk.Label(root, text="לא ניתן לטעון את התמונה", fg="red").pack()

root.mainloop()

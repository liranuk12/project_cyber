import subprocess
import time
import os
import sys

def run_server():
    """מריץ את השרת בחלון נפרד"""
    print("🚀 Starting server...")
    if sys.platform.startswith("win"):
        subprocess.Popen(["start", "cmd", "/k", "python server.py"], shell=True)
    else:
        subprocess.Popen(["python3", "server.py"])

def run_client_app():
    """מריץ את האפליקציה הראשית (FUTRADE)"""
    print("🪟 Launching FUTRADE app...")
    os.system("python welcome_screen.py")

if __name__ == "__main__":
    run_server()
    time.sleep(2)  # נותן לשרת זמן להיטען
    run_client_app()

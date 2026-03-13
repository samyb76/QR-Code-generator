import qrcode
import tkinter as tk
from tkinter import filedialog
import ctypes
import sys

if sys.platform == "win32":
    ctypes.windll.shcore.SetProcessDpiAwareness(2)

root = tk.Tk()
root.withdraw()

root.lift()
root.attributes("-topmost", True)
root.focus_force()

data = input("Entre un lien ou un texte : ")

img = qrcode.make(data)

file_path = filedialog.asksaveasfilename(
    defaultextension=".png",
    filetypes=[("Image PNG", "*.png")],
    title="QR Code Generator",
    parent=root,
)

if file_path:
    img.save(file_path)
    print("QR code enregistré :", file_path)
else:
    print("Sauvegarde annulée")

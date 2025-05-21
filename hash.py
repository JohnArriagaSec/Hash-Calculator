import hashlib
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path_ = filedialog.askopenfilename(title="select a file to analyze", filetypes=[("All Files", "*.*")])

if file_path_:
    with open (file_path_, "rb") as file:
        file_bytes = file.read()
        hash_result = hashlib.md5(file_bytes).hexdigest()
        print("MD5 HASH:", hash_result)

else:
    print("NO FILE SELECTED")

input("press enter to exit: ")

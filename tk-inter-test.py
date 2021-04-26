import tkinter as tk
from tkinter import filedialog, simpledialog, colorchooser

root = tk.Tk()
root.withdraw()

# test = simpledialog.askstring('Asking for a string', 'Enter a string')

# print(test)

filenames = filedialog.askopenfilenames()

print(type(filenames))

for filename in filenames: print(f'Name: {filename}')

colour = colorchooser.askcolor()

import tkinter as tk
from tkinter import filedialog

from pathlib import Path

import chardet

window = tk.Tk()
window.withdraw()

filename = Path(filedialog.askopenfilename())

if filename:
    with open(filename, 'rb') as file:
        print(filename)
        det = chardet.UniversalDetector()

        for line in file:
            det.feed(line)
            if det.done: break
        
        det.close()
        print(det.result)
else:
    print('No filename specified')

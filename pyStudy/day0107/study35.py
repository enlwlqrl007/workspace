import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title('파일 대화상자1')
window.geometry('400x100')

fileName = askopenfilename(parent=window, filetypes=(('GIF파일', '*.gif'),('모든파일', '*.*')))

label1 = tk.Label(window, text=fileName)
label1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

window.mainloop()
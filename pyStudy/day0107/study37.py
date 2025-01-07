# 이미지 선택하기2
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title('파일 대화상자3')
window.geometry('400x100')

file = askopenfile(parent=window, filetypes=(('GIF파일', '*.gif'),('모든파일', '*.*')))

label1 = tk.Label(window, text=file)
label1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

label2 = tk.Label(window, text=file.name)
label2.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

window.mainloop()
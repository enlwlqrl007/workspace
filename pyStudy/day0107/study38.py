# 폴더 선택하기
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title('파일 대화상자4')
window.geometry('400x100')

myDir = askdirectory(parent=window, title='내 폴더 선택하기')

label1 = tk.Label(window, text=myDir)
label1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

window.mainloop()
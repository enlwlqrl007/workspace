# 이미지 선택하기1
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title('파일 대화상자2')
window.geometry('400x100')

fileNames = askopenfilenames(parent=window, filetypes=(('GIF파일', '*.gif'),('모든파일', '*.*')))

labelList =[]
index = 0
for fileName in fileNames:
    labelList.append(tk.Label(window, text=fileName))
    labelList[index].pack(expand=1, anchor=tk.CENTER, side=tk.TOP)
    index += 1

window.mainloop()
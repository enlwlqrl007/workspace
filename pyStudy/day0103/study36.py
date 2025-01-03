import tkinter as tk
from tkinter import ttk
import random

btnList = [''] * 9
fnameList = []
for i in range(9):
    fnameList.append('img' + str(i)+'.gif')
random.shuffle(fnameList)
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = tk.Tk()
window.title("고정 위치 배치2")
window.geometry("768x768")

for i in range(9):
    photoList[i] = tk.PhotoImage(file="day0103/gif/" + fnameList[i])
    btnList[i] = ttk.Button(window, image=photoList[i])

for i in range(3):
    for k in range(3):
        btnList[num].place(x=xPos,y=yPos)
        num += 1
        xPos += 256
    xPos = 0
    yPos += 256

window.mainloop()
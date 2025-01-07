# 이벤트(좌표 2개로 선 긋기 + 색상지정)
import tkinter as tk
from tkinter.colorchooser import * # 색상 선택 툴

def mouseDown(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y1, x2, y2, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1,y1, x2,y2, fill=penColor)

def clickButton():
    global penColor
    color = askcolor()
    penColor = color[1]


x1, y1, x2, y2 = 0,0,0,0
penColor = None

window = tk.Tk()
window.title('마우스 이벤트9')
window.geometry('400x400')

button1 = tk.Button(window, text='색상선택', command=clickButton)
button1.pack()

canvas = tk.Canvas(window, width=400, height=400)
canvas.bind('<Button-1>', mouseDown)
canvas.bind('<ButtonRelease-1>', mouseDrop)
canvas.pack()

window.mainloop()
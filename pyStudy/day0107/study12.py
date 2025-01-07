# 이벤트(좌표 2개로 선 긋기 + 색상지정 총합)
import tkinter as tk
from tkinter.colorchooser import * # 색상 선택 툴

def clickButton():
    global penColor
    color = askcolor()
    penColor = color[1]

def mouseDown(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def leftMouseDrop(event):
    global x1, y1, x2, y2,penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1,y1, x2,y2, fill=penColor)

def midMouseDrop(event):
    global x1, y1, x2, y2,penColor
    x2 = event.x
    y2 = event.y
    canvas.create_oval(x1,y1, x2,y2, outline=penColor)

def rightMouseDrop(event): # 라인으로 사각형 만들기(좌표 5개)
    global x1, y1, x2, y2,penColor
    x2 = event.x
    y2 = event.y
    if(x1 > x2):
        x1,x2 = x2,x1
    if(y1 > y2):
        y1,y2 = y2,y1
    canvas.create_line(x1,y1, x1,y2, x2,y2, x2,y1, x1,y1, outline=penColor)

x1, y1, x2, y2 = 0,0,0,0
penColor = None

window = tk.Tk()
window.title('마우스 이벤트10')
window.geometry('400x400')

button1 = tk.Button(window, text='색상선택', command=clickButton)
button1.pack()

canvas = tk.Canvas(window, width=400, height=400)
canvas.bind('<Button-1>', mouseDown)
canvas.bind('<ButtonRelease-1>', leftMouseDrop)
canvas.bind('<Button-2>', mouseDown)
canvas.bind('<ButtonRelease-2>', midMouseDrop)
canvas.bind('<Button-3>', mouseDown)
canvas.bind('<ButtonRelease-3>', rightMouseDrop)
canvas.pack()

window.mainloop()
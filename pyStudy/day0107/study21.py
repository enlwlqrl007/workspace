# 키보드 이벤트(F1,F2 ~ F12까지 눌렀을때 색상변경)
import tkinter as tk
import random

def pressKey(event):
    global penColor
    key = event.keycode
    colorList = ['red', 'yellow','green', 'blue','black', 'magenta']
    if(112<=key<=123):
        penColor = colorList[(key-112) % len(colorList)]

    if(key==9):
        penColor = random.choic(colorList)

def mouseDown(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y1, x2, y2,penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, fill=penColor)
    
window = tk.Tk()
window.title('키보드 이벤트9')
window.geometry('400x400')
x1, y1, x2, y2 = 0, 0, 0, 0
penColor = 'black'

canvas = tk.Canvas(window, width=400, height=400)
canvas.bind('<Button-1>', mouseDown)
canvas.bind('<ButtonRelease-1>', mouseDrop)
canvas.pack()

window.bind('<Key>', pressKey)

window.mainloop()   
# 이벤트(좌표 2개로 원형)
import tkinter as tk

def mouseDown(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y1, x2, y2
    x2 = event.x
    y2 = event.y
    canvas.create_oval(x1,y1, x2,y2)

x1, y1, x2, y2 = 0,0,0,0

window = tk.Tk()
window.title('마우스 이벤트7')
window.geometry('400x400')

canvas = tk.Canvas(window, width=400, height=400)
canvas.bind('<Button-1>', mouseDown)
canvas.bind('<ButtonRelease-1>', mouseDrop)
canvas.pack()

window.mainloop()
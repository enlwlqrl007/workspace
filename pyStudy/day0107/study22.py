# 키보드 이벤트(키보드로 그림그리기)
import tkinter as tk


def pressKey(event):
    global x1, y1, x2, y2
    key = event.keycode
    if key == 37:
        x2 = x1 -10
    elif key == 38:
        y2 = y1 - 10
    elif key == 39:
        x2 = x1 + 10
    elif key == 40:
        y2 = y1 + 10
    cavas.create_line(x1, y1, x2, y2)
    x1, y1 = x2, y2

window = tk.Tk()
window.title('키보드 이벤트10')
window.geometry('400x400')

x1, y1, x2, y2 = 200,200,200,200

cavas = tk.Canvas(window, width=400, height=400)
cavas.pack()


window.bind('<Key>', pressKey)


window.mainloop()
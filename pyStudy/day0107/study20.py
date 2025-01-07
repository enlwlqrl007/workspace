# 키보드 이벤트()
import tkinter as tk

def pressKey(event):
    global curX, curY
    key = event.keycode
    if(key==37):
        curX -= 10
    elif(key==38):
        curY -= 10
    elif(key==39):
        curX += 10
    elif(key==40):
        curY += 10
    label1.place(x=curX, y=curY)

window = tk.Tk()
window.title('키보드 이벤트8')
window.geometry('400x400')

curX, curY = 100, 100
photo = tk.PhotoImage(file='day0103\gif\키키.gif')
label1 = tk.Label(window, image=photo, width=150, height=150)
label1.place(x=curX, y=curY)

window.bind('<Up>', pressKey)
window.bind('<Down>', pressKey)
window.bind('<Left>', pressKey)
window.bind('<Right>', pressKey)

window.mainloop()   
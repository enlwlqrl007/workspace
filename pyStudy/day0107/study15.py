# 키보드 이벤트(버튼 배경을 이미지로)(Tab누르고 키보드 눌리고 사용)
import tkinter as tk
from tkinter import messagebox

def pressKey1(event):
    if(event.keycode==9):
        return
    messagebox.showinfo('키보드', '## 호랑이에서 키눌림')

def pressKey2(event):
    if(event.keycode==9):
        return
    messagebox.showinfo('키보드', '$$ 사자에서 키눌림')
    
window = tk.Tk()
window.title('키보드 이벤트3')
window.geometry('400x400')

photo1 = tk.PhotoImage(file='day0103\gif\호랑이.gif')
button1 = tk.Button(window, image=photo1, width=150, height=150)
button1.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)
button1.bind('<Key>', pressKey1)

photo2 = tk.PhotoImage(file='day0103\gif\사자.gif')
button2 = tk.Button(window, image=photo2, width=150, height=150)
button2.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)
button2.bind('<Key>', pressKey2)

window.mainloop()
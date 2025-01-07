# 키보드 이벤트(누른키 아스키코드로 나타내기)
import tkinter as tk
from tkinter import messagebox

def pressKey(event):
    key = str(event.keycode)
    messagebox.showinfo('키보드', str(key) + '를 누름')

window = tk.Tk()
window.title('키보드 이벤트2')

window.bind('<Key>', pressKey)

window.mainloop()
# 키보드 이벤트(모든 키보드)
import tkinter as tk
from tkinter import messagebox

def pressKey(event):
    messagebox.showinfo('키보드', '키보드를 누름')

window = tk.Tk()
window.title('키보드 이벤트1')

window.bind('<Key>', pressKey)

window.mainloop()
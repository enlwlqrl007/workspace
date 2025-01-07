# 이벤트(이미지에 클릭 이벤트)
import tkinter as tk
from tkinter import messagebox

def clickMouse(event):
    messagebox.showinfo('마우스','그림에서 마우스가 클릭됨')

window = tk.Tk()
window.title('마우스 이벤트3')
window.geometry('400x400')

photo = tk.PhotoImage(file='day0103\gif\호랑이.gif')
label1 = tk.Label(window, image=photo)
label1.pack(expand=1, anchor=tk.CENTER)

label1.bind('<Button>', clickMouse)

window.mainloop()
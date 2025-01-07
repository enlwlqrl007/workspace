# 이벤트(이미지에 마우스 올리고 내렸을때 이미지 변경 이벤트)
import tkinter as tk
from tkinter import messagebox

def enterMouse(event):
    photo = tk.PhotoImage(file="day0103\gif\사자.gif") # 마우스를 올렸을때 이미지
    label1.configure(image=photo)
    label1.image=photo

def leaveMouse(event):
    photo = tk.PhotoImage(file="day0103\gif\강아지.gif") # 마우스를 내렸을때 이미지
    label1.configure(image=photo)
    label1.image=photo

window = tk.Tk()
window.title('마우스 이벤트4')
window.geometry('400x400')

photo = tk.PhotoImage(file='day0103\gif\호랑이.gif') # 기본 이미지
label1 = tk.Label(window, image=photo)
label1.pack(expand=1, anchor=tk.CENTER)

label1.bind('<Enter>', enterMouse) # 마우스를 올렸을때
label1.bind('<Leave>', leaveMouse) # 마우스를 내렸을때

window.mainloop()
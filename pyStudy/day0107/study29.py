# 메시지 상자
import tkinter as tk
from tkinter import messagebox

def click_button1():
    messagebox.showinfo('정보', '정보입니다.')

def click_button2():
    messagebox.showwarning('경고', '경고입니다.')

def click_button3():
    messagebox.showerror('요류', '오류입니다.')

window = tk.Tk()
window.title('메시지 상자')
window.geometry('300x100')

button1 = tk.Button(window, text='정보 메시지', command=click_button1)
button1.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)
button2 = tk.Button(window, text='경고 메시지', command=click_button2)
button2.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)
button3 = tk.Button(window, text='오류 메시지', command=click_button3)
button3.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)

window.mainloop()
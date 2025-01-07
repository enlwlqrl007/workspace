# 키보드 이벤트(아스키코드로 키보드 이벤트)
import tkinter as tk

def pressKey(event):
    key = event.keycode
    if(key==27): #ESC키
        entryStr.set('')

window = tk.Tk()
window.title('키보드 이벤트4')
window.geometry('400x400')

entryStr = tk.StringVar()
entry = tk.Entry(window, textvariable=entryStr)
entry.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)
entry.bind('<Key>', pressKey)

window.mainloop()
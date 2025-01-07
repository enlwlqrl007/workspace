# 키보드 이벤트()
import tkinter as tk

def pressKey(event):
    key = event.keycode
    entryStr1.set(key)

window = tk.Tk()
window.title('키보드 이벤트6')
window.geometry('150x150')

entryStr1 = tk.StringVar()
entry1 = tk.Entry(window, textvariable=entryStr1)
entry1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)
entry1.bind('<Key>', pressKey)

window.mainloop()
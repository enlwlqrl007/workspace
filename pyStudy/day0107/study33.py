# 서브 윈도우 창
import tkinter as tk

def openSubWindow():
    sub = tk.Toplevel(window)
    sub.geometry('200x100')
    sub.title('서브 윈도우창')
    sub.grab_set()

    label = tk.Label(sub, text='서브 윈도우창이 열렸습니다.')
    label.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)

window = tk.Tk()
window.title('메인 윈도우창')
window.geometry('300x300')

button = tk.Button(window, text='서브 윈도우 열기', command=openSubWindow)
button.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)

window.mainloop()
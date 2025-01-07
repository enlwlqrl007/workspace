# 이벤트
import tkinter as tk
from tkinter import messagebox

def clickLeft(event): # event = 어떤 마우스를 클릭했는지, 클릭한 좌표가 어디인지 내용이 다 포함
    messagebox.showinfo('마우스','마우스 왼쪽 버튼 클릭')

window = tk.Tk()
window.title('마우스 이벤트1')

window.bind('<Button-1>', clickLeft)

window.mainloop()
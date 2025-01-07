# 메뉴만들기(메뉴를 통해 메시지박스, 종료)
import tkinter as tk
from tkinter import messagebox

def func_open():
    messagebox.showinfo('메뉴선택', '열기 선택')

def func_exit():
    window.quit()
    window.destroy()

window = tk.Tk()
window.title('메뉴5')
window.geometry('400x400')

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

fileMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=func_open)
fileMenu.add_command(label='저장')
fileMenu.add_command(label='종료',command=func_exit)

window.mainloop()
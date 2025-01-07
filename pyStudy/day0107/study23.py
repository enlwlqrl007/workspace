# 메뉴만들기
import tkinter as tk

window = tk.Tk()
window.title('메뉴1')

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

fileMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기')
fileMenu.add_separator()
fileMenu.add_command(label='종료',command=exit)

window.mainloop()
# 메뉴만들기(우측마우스, Ctrl+X 후 좌클릭 한지역에서 나타내기)
import tkinter as tk

def popup_func(event):
    editMenu.tk_popup(event.x_root, event.y_root)

def popup_func2(event):
    fileMenu.tk_popup(event.x_root, event.y_root)


window = tk.Tk()
window.title('메뉴4')
window.geometry('400x400')

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

fileMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기')
fileMenu.add_separator()
fileMenu.add_command(label='종료',command=exit)

editMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='편집', menu=editMenu)
editMenu.add_command(label='잘라내기')
editMenu.add_command(label='복사')
editMenu.add_command(label='붙여넣기')

window.bind('<Button-3>', popup_func) # 우클릭
window.bind('<Button-1>', popup_func2) # 좌클릭

window.mainloop()
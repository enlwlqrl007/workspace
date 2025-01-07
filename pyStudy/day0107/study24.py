# 메뉴만들기
import tkinter as tk

window = tk.Tk()
window.title('메뉴2')

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

fileMenu = tk.Menu(mainMenu, tearoff=0) # tearoff=0를 사용하면 -------(줄눈금)이 사라짐
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기')
fileMenu.add_separator()
fileMenu.add_command(label='종료',command=exit)

editMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='편집', menu=editMenu)
editMenu.add_command(label='잘라내기')
editMenu.add_command(label='복사')
editMenu.add_command(label='붙여넣기')

helpMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='도움말', menu=helpMenu)
helpMenu.add_command(label='도움말 보기')
helpMenu.add_separator()
helpMenu.add_command(label='About...')

window.mainloop()
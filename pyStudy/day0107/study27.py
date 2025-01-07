# 메뉴만들기(메뉴로 투명도 조절)
import tkinter as tk

def alpha_up():
    value = window.attributes('-alpha')
    window.wm_attributes('-alpha', value-0.1)

def alpha_down():
    value = window.attributes('-alpha')
    window.wm_attributes('-alpha', value+0.1)

window = tk.Tk()
window.title('메뉴6')
window.geometry('400x400')

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

alphaMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='윈도우창 투명도', menu=alphaMenu)
alphaMenu.add_command(label='중가', command=alpha_up)
alphaMenu.add_separator()
alphaMenu.add_command(label='감소', command=alpha_down)

window.mainloop()
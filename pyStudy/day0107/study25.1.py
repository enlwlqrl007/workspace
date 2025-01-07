# 메뉴만들기(우측마우스, Ctrl+X 후 좌클릭 한지역에서 나타내기)
import tkinter as tk

def popup_func(event):
    popup.tk_popup(event.x_root, event.y_root)

window = tk.Tk()
window.title('메뉴3')
window.geometry('400x400')

popup= tk.Menu(window, tearoff=0)
popup.add_command(label='열기')
popup.add_command(label='저징')
popup.add_separator()
popup.add_command(label='종료', command=exit)

window.bind('<Button-3>', popup_func) # 우클릭
window.bind('<Control-x>', popup_func) # Ctrl+X 후 좌클릭

window.mainloop()
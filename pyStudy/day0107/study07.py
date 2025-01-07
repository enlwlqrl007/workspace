# 이벤트(좌표, 버튼을 받아와 글자 변경)
import tkinter as tk

def clickMouse(event):
    txt = ''
    if (event.num==1):
        txt += '마우스 왼쪽 버튼이 ('
    elif (event.num==2):
        txt += '마우스 가운데 버튼이 ('
    else:
        txt += '마우스 오른쪽 버튼이 ('
    txt += str(event.x) + ',' + str(event.y) + ')에서 클릭됨'
    label1.configure(text=txt)

window = tk.Tk()
window.title('마우스 이벤트5')
window.geometry('400x400')

label1 = tk.Label(window, text='이곳이 바뀜')
label1.pack(expand=1, anchor=tk.CENTER)

window.bind('<Button>', clickMouse)

window.mainloop()
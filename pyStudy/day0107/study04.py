# 이벤트
import tkinter as tk
from tkinter import messagebox

def clickButton(event): # event = 어떤 마우스를 클릭했는지, 클릭한 좌표가 어디인지 내용이 다 포함
    if(event.num == 1): # num==1 => 마우스 왼쪽버튼
        messagebox.showinfo('마우스','마우스 왼쪽 버튼 클릭')
    elif(event.num == 2): # num==2 => 마우스 가운데버튼(스크롤)
        messagebox.showinfo('마우스','마우스 가운데 버튼클릭')
    else: # num==3 => 마우스 오른쪽버튼
        messagebox.showinfo('마우스','마우스 오른쪽 버튼클릭')
        
window = tk.Tk()
window.title('마우스 이벤트2')

window.bind('<Button>', clickButton)


window.mainloop()
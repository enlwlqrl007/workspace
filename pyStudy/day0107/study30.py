# 메시지 상자(여러가지 질문의 답을 나타내기)
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('메시지 상자2')
window.geometry('300x150')

ret1 = messagebox.askquestion('askquestion', '선택하세요')
ret2 = messagebox.askokcancel('askokcancel', '선택하세요')
ret3 = messagebox.askretrycancel('askretrycancel', '선택하세요')
ret4 = messagebox.askyesno('askyesno', '선택하세요')
ret5 = messagebox.askyesnocancel('askyesnocancel', '선택하세요')

retStr = ret1 + '\n'
retStr += str(ret2) + '\n'
retStr += str(ret3) + '\n'
retStr += str(ret4) + '\n'
retStr += str(ret5) 

label = tk.Label(window, text=retStr)
label.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)

window.mainloop()
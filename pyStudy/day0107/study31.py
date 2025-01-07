# 메시지상자(입력값을 받아 나타내기)
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.title('표준 입력 대화 상자1')
window.geometry('300x150')

floatVal = simpledialog.askfloat('실수 입력', '실수를 입력하세요')
intVal = simpledialog.askinteger('정수 입력', '정수를 입력하세요')
strVal = simpledialog.askstring('문자열 입력', '문자열를 입력하세요')

retStr = str(floatVal) + '\n'
retStr += str(intVal) + '\n'
retStr += str(strVal)

label = tk.Label(window, text=retStr)
label.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)

window.mainloop()
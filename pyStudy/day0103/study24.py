# 라디오 버튼
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("라디오버튼1");

label1 = ttk.Label(window, text="직업을 선택하세요(한개만 가능)");
label1.grid(row=0,column=0,columnspan=3);

rdoVar = tk.IntVar()

radio1 = ttk.Radiobutton(window, variable=rdoVar, value=1, text="학생");
radio1.grid(row=1,column=0)
radio2 = ttk.Radiobutton(window, variable=rdoVar, value=2, text="회사원");
radio2.grid(row=1,column=1)
radio3 = ttk.Radiobutton(window, variable=rdoVar, value=3, text="자영업");
radio3.grid(row=1,column=2)



window.mainloop()
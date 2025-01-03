import tkinter as tk
from tkinter import ttk

def click_button():
    exprStr = str(num1.get()) + combo1.get() + str(num2.get())
    resVal = eval(exprStr)
    label2.configure(text=str(resVal));

window = tk.Tk()
window.title("육칙연산 계산기")

# 두 개의 숫자 받음
num1 = tk.DoubleVar()
num2 = tk.DoubleVar()

lable1 = ttk.Label(window, text="계산할 숫자 및 연사자를 입력하세요.",font=("맑은고딕",16))
lable1.grid(row=0, column=0, columnspan=3)

entry1 = ttk.Entry(window, width=10, textvariable=num1).grid(row=1,column=0);
combo1 = ttk.Combobox(window, width=10)
combo1.grid(row=1, column=1)
combo1["values"]=('+', '-', '*', '/', '%', '**')
entry2 = ttk.Entry(window, width=10, textvariable=num2).grid(row=1,column=2);
button1 = ttk.Button(window, text="=", width=30, command=click_button).grid(row=2, column=0, columnspan=3)
label2 = ttk.Label(window, text="결과값 : ",foreground='red',font=("맑은고딕",14))
label2.grid(row=3,column=0);


window.mainloop()
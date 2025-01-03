import tkinter as tk
from tkinter import ttk

def click_button():
    resValue = intValue1.get() + intValue2.get()
    label2.configure(text=str(resValue));

window = tk.Tk()
window.title("덧셈 계산기")

intValue1 = tk.IntVar();
intValue2 = tk.IntVar();

label1 = ttk.Label(window, text="값을 입력하세요!!").grid(row=0, column=0);
entry1 = ttk.Entry(window, width=15, textvariable=intValue1).grid(row=1,column=0);
entry2 = ttk.Entry(window, width=15, textvariable=intValue2).grid(row=1,column=1);
button1 = ttk.Button(window, text="+",command=click_button).grid(row=2,column=0);
label2 = ttk.Label(window, text="결과 값 : ")
label2.grid(row=3, column=0);

window.mainloop()   
# grid
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("ttk 화면 배치")

btn1 = ttk.Button(window, text="버튼1").grid(row=0,column=0);
btn2 = ttk.Button(window, text="버튼2").grid(row=0,column=1);
btn3 = ttk.Button(window, text="버튼3").grid(row=1,column=0);
btn4 = ttk.Button(window, text="버튼4").grid(row=1,column=1);
btn5 = ttk.Button(window, text="버튼5",command=quit).grid(row=2,column=2);


window.mainloop()
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("텍스트 상자2")

label1 = ttk.Label(window, text="값을 입력하세요!").grid(row=0,column=0);
entry1 = ttk.Entry(window).grid(row=1,column=0);
button1 = ttk.Button(window, text="클릭하세요.").grid(row=1,column=1);


window.mainloop()
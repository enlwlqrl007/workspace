import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("텍스트 상자1")

entry1 = ttk.Entry(window).grid(row=0,column=0);    # input이랑 비슷


window.mainloop()
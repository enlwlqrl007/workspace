import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("콤보 박스");
combo1 = ttk.Combobox(window)
combo1.grid(row=0,column=0);
combo1["values"] = [2,3,5,6,7,11,13,17]
combo2 = ttk.Combobox(window, state='readonly')
combo2.grid(row=0, column=1);
combo2["values"] = ("red","green","blue")

window.mainloop()
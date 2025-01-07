# 탭
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('탭 위젯1')

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='탭1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='탭2')

tabControl.pack(expand=1, fill='both', padx=10, pady=10)

button1 = tk.Button(tab1, text='버튼1', bg='yellow')
button1.grid(row=0, column=0, padx=50, pady=50)
button2 = tk.Button(tab2, text='버튼2', bg='green')
button2.grid(row=0, column=0, padx=50, pady=50)

window.mainloop()
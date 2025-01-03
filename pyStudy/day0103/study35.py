# place()
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("고정 위치 배치1")
window.geometry("300x300")

button1 = ttk.Button(window, text="버튼1")
button2 = ttk.Button(window, text="버튼2")
button3 = ttk.Button(window, text="버튼3")

button1.place(x=0, y=0)
button2.place(x=100, y=100)
button3.place(x=200, y=200)

window.mainloop()
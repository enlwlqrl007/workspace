import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("폭 조정")

button1 = tk.Button(window, text="버튼1", width=30 ,height=10)
button2 = tk.Button(window, text="버튼2", width=30 ,height=10)
button3 = tk.Button(window, text="버튼3", width=30 ,height=10)

# fill=tk.Y  -> 창이 늘어나도 세로부분을 꽉채움 
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT) 
button3.pack(side=tk.LEFT)

window.mainloop()
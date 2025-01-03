import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("폭 조정")

button1 = ttk.Button(window, text="버튼1")
button2 = ttk.Button(window, text="버튼2")
button3 = ttk.Button(window, text="버튼3")

# fill=tk.X  -> 창이 늘어나도 가로부분을 꽉채움 
button1.pack(side=tk.TOP, fill=tk.X)
button2.pack(side=tk.TOP, fill=tk.X)
button3.pack(side=tk.TOP, fill=tk.X)

window.mainloop()
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("폭 조정")
window.geometry("260x200")

button1 = ttk.Button(window, text="버튼1")
button2 = ttk.Button(window, text="버튼2")
button3 = ttk.Button(window, text="버튼3")

# fill=tk.Y  -> 창이 늘어나도 세로부분을 꽉채움 
button1.pack(side=tk.LEFT, fill=tk.Y)
button2.pack(side=tk.LEFT, fill=tk.Y)
button3.pack(side=tk.LEFT, fill=tk.Y)

window.mainloop()
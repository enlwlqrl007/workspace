# pack()
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("수평정렬")

# button1 = tk.Button(window, text="버튼1")
# button2 = tk.Button(window, text="버튼2")
# button3 = tk.Button(window, text="버튼3")

# ttk를 사용하면 버튼이 여유있게 표현됨
button1 = ttk.Button(window, text="버튼1")
button2 = ttk.Button(window, text="버튼2")
button3 = ttk.Button(window, text="버튼3")

button1.pack(side=tk.RIGHT)
button2.pack(side=tk.RIGHT)
button3.pack(side=tk.RIGHT)


window.mainloop()


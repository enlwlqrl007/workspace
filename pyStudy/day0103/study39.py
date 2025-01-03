import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("레이블 프레임3")

frame1 = ttk.Labelframe(window, text="부모프레임")
frame1.grid(row=0, column=0, padx=10, pady=10)

button1 = ttk.Button(frame1, text="버튼1").grid(row=0, column=0)
button2 = ttk.Button(frame1, text="버튼2").grid(row=0, column=1)
button3 = ttk.Button(frame1, text="버튼3").grid(row=0, column=2)

subFrame1 = ttk.LabelFrame(frame1, text="자식프레임1")
subFrame1.grid(row=1, column=0, padx=10, pady=10)

label1 = ttk.Label(subFrame1, text="레이블1").grid(row=0, column=0)
label2 = ttk.Label(subFrame1, text="레이블2").grid(row=0, column=1)

subFrame2 = ttk.LabelFrame(frame1, text="자식프레임2")
subFrame2.grid(row=1, column=1, padx=10, pady=10)

rdoVar = tk.IntVar()
radio1 = ttk.Radiobutton(subFrame2, text="라디오1").grid(row=0, column=0)
radio2 = ttk.Radiobutton(subFrame2, text="라디오2").grid(row=0, column=1)
radio3 = ttk.Radiobutton(subFrame2, text="라디오3").grid(row=0, column=2)

imageLabel = ttk.Label(window)
imageLabel.grid(row=2, column=0, columnspan=3)

window.mainloop()
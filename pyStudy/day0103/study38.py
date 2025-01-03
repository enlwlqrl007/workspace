import tkinter as tk
from tkinter import ttk

def cilck_button():
    if(rdoVar.get() == 1):
        fileName = "day0103\gif\dog.PNG"
    elif(rdoVar.get() == 2):
        fileName = "day0103\gif\cat.PNG"
    else:
        fileName = "day0103/gif/tg.PNG"

    photo = tk.PhotoImage(file = fileName)
    imageLabel.configure(image=photo)
    imageLabel.image = photo

window = tk.Tk()
window.title("레이블 프레임2")

frame1 = ttk.Labelframe(window, text="좋아하는 동물은?")
frame1.grid(row=0,column=0, padx=10, pady=10)

rdoVar = tk.IntVar()
radio1 = ttk.Radiobutton(frame1, variable=rdoVar, value=1, text="강아지")
radio1.grid(row=0, column=0)
radio2 = ttk.Radiobutton(frame1, variable=rdoVar, value=2, text="고양이")
radio2.grid(row=0, column=1)
radio3 = ttk.Radiobutton(frame1, variable=rdoVar, value=3, text="호랑이")
radio3.grid(row=0, column=2)

button1 = ttk.Button(window, text="클릭하세요!", command=cilck_button)
button1.grid(row=1, column=0, columnspan=3)

imageLabel = ttk.Label(window)
imageLabel.grid(row=2, column=0, columnspan=3)

window.mainloop()
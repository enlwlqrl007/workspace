import tkinter as tk
from tkinter import ttk

def click_button():
    resValue = combo1.get()
    entryStr.set(resValue)

window = tk.Tk()
window.title("콤보박스2");

label1 = ttk.Label(window, text="좋아하는 동물 선택").grid(row=0,column=0);
entryStr = tk.StringVar()
entry1 = ttk.Entry(window, width=20,textvariable=entryStr,state="disabled")
entry1.grid(row=1,column=0);
combo1 = ttk.Combobox(window)
combo1.grid(row=1,column=1)
combo1["values"] = ("강아지","고양이","호랑이","여우","판다")
button1 = ttk.Button(window, text="클릭하세요.",command=click_button).grid(row=1,column=2);




window.mainloop()
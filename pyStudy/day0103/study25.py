import tkinter as tk
from tkinter import ttk

def click_button():
    if(rdoVar.get() == 1):
        entryStr.set('강아지')
    if(rdoVar.get() == 2):
        entryStr.set('고양이')
    if(rdoVar.get() == 3):
        entryStr.set('거북이')

window = tk.Tk()
window.title("라디오버튼2")

label1 = ttk.Label(window, text="좋아하는 동물선택(한개 선택가능!)")
label1.grid(row=0,column=0,columnspan=3);

rdoVar = tk.IntVar()
radio1 = ttk.Radiobutton(window, variable=rdoVar, value=1, text="강아지")
radio1.grid(row=1,column=0)
radio2 = ttk.Radiobutton(window, variable=rdoVar, value=2, text="고양이")
radio2.grid(row=1,column=1)
radio3 = ttk.Radiobutton(window, variable=rdoVar, value=3, text="거북이")
radio3.grid(row=1,column=2)

button1 = ttk.Button(window, text="클릭하세요!", command=click_button)
button1.grid(row=2,column=0,columnspan=3);

entryStr = tk.StringVar()
entry1 = ttk.Entry(window, width=20, textvariable=entryStr, state='disabled')
entry1.grid(row=3, column=0, columnspan=3);


window.mainloop()
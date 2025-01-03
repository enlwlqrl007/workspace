import tkinter as tk
from tkinter import ttk

def click_button():
    if(str(entry1['state']) == 'normal'):
        entry1.configure(state='disable');
        button1.configure(bg="red");
    else:
        entry1.configure(state="normal")
        button1.configure(bg="green");

window = tk.Tk()
window.title("엔트리 비활성화");

label1 = ttk.Label(window, text="값을 입력하세요.").grid(row=0, column=0);
entry1 = ttk.Entry(window, width=20)
entry1.grid(row=1,column=0)
button1 = tk.Button(window, text="클릭하세요.",command="click_button")
button1.grid(row=1,column=1);\


window.mainloop()
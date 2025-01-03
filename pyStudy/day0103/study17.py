import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def click_button():
    messagebox.showinfo("엔트리 입력값","입력한 값은[" + inputValue.get()+ "] 입니다.")

window = tk.Tk()
window.title("텍스트 상자3");

inputValue = tk.StringVar()

label1 = ttk.Label(window, text="값을 입력하세요!").grid(row=0,column=0);
entry1 = ttk.Entry(window, width=20, textvariable=inputValue).grid(row=1, column=0);
button1 = ttk.Button(window,text="클릭하세요.",command=click_button).grid(row=1,column=1);

window.mainloop()
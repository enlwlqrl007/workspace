import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("레이블5");
window.geometry("300x200");

label1 = ttk.Label(window, text="TTK 연습1", font=("굴림체",18))
label2 = ttk.Label(window, text="TTK 연습2", font=("궁서체",20),
                   relief="raised",cursor='watch')
label3 = ttk.Label(window, text="TTK 연습3", font=("맑은고딕",30),background="magenta")

label1.pack();
label2.pack();
label3.pack();

window.mainloop()
import tkinter as tk
from tkinter import messagebox

def click_button():
    messagebox.showinfo("버튼 누름","버튼을 눌렀어요^o^")   # 첫번째는 메세지박스의 타이틀, 두번째는 메세지박스의 내용

window = tk.Tk()
window.title("버튼3");
button1 = tk.Button(window, text="여기를 클릭",command=click_button);
button1.pack();

window.mainloop()
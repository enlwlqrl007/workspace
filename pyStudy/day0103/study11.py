import tkinter as tk

def click_button():
    label1.configure(font=("궁서체",40))
    label1.configure(text="버튼 눌렀음", fg = "red");
    label1.configure(state='disabled');

window = tk.Tk()
window.title("버튼4");
window.geometry("300x200");

label1 = tk.Label(window, text="이 글자가 봐뀜!");
label1.pack();

button1 = tk.Button(window, text="버튼을 누르세요!",command=click_button);
button1.pack();


window.mainloop()
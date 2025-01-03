import tkinter as tk
from tkinter import messagebox

def click_button():
    messagebox.showinfo("이미지 버튼을 누름","사진이 봐뀝니다^^.");
    photo = tk.PhotoImage(file="day0103\gif\jj.PNG");
    button1.configure(image=photo);
    button1.image = photo;

window = tk.Tk()
window.title("버튼5");
window.geometry("500x300");

photo = tk.PhotoImage(file="day0103/gif/bb.jpg");
button1 = tk.Button(window, image=photo, command=click_button);
button1.pack();

window.mainloop()
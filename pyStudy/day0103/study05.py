import tkinter as tk

window = tk.Tk()
window.title("레이블3");

photo = tk.PhotoImage(file="day0103/gif/bb.jpg");

# image 옵션 우선, text는 무시
photoLabel = tk.Label(window, text="부산-갈맷길풍경",image=photo);  

photoLabel.pack();

window.mainloop()
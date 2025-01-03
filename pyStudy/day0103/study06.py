import tkinter as tk

window = tk.Tk()
window.title("레이블4")

photo1 = tk.PhotoImage(file="day0103/gif/bb.jpg");
photo2 = tk.PhotoImage(file="day0103/gif/jj.PNG");
photoLabel1 = tk.Label(window, image=photo1);
photoLabel2 = tk.Label(window, image=photo2);

photoLabel1.pack();
photoLabel2.pack();

window.mainloop()   

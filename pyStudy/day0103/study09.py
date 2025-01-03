import tkinter as tk

window = tk.Tk()
window.title("버튼2");
button2 = tk.Button(window, text="프로그램 종료",command=quit);     # command 명령어 -> quit : 종료
button2.pack();

window.mainloop()
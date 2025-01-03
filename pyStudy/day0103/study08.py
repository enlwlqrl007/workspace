# 버튼 위젯

import tkinter as tk

window = tk.Tk()
window.title("버튼1");

button1 = tk.Button(window, text="눌러봐",fg="skyblue");
button1.pack();

window.mainloop()
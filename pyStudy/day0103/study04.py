import tkinter as tk

window = tk.Tk()
window.title("레이블2");
window.geometry("500x300");

label1 = tk.Label(window, text="오늘은");
label2 = tk.Label(window, text="날씨가", font=("궁서체",20),fg="skyblue");                  # fg : 글씨색상
label3 = tk.Label(window, text="좋아",bg="pink",width=20,height=5,anchor=tk.W);            # bg : 배경색상, anchor : 방향   // N 북쪽, S 남쪽, E 동쪽, W 서쪽  // center는 기본값!

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
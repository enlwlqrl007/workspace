# 체크박스
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("체크박스");

label1 = ttk.Label(window, text="취미를 선택하세요(중복가능).")
label1.grid(row=0,column=0,columnspan=3);   # 체크 버튼 3개를 한칸에 대응하기 위함

check1 = tk.Checkbutton(window, text="등산")
check1.grid(row=1,column=0);
check1.select()                             # 초기값으로 선택되어있음

check2 = tk.Checkbutton(window, text="낚시",state="disabled")       # disabled : 비 활성화
check2.grid(row=1,column=1)
check2.deselect()                           # 초기에 선택이 안되있음

check3 = tk.Checkbutton(window, text="독서")
check3.grid(row=1,column=2);
check3.deselect()


window.mainloop()
#레이블 위젯
import tkinter as tk

window = tk.Tk()
window.title("레이블1");

label1 = tk.Label(window, text="Python의 GUI!!");       # 사용하려면 레이블 위젯을 선언 해줘야함!
label1.pack()                                           # 보이게 하기 위해 pack코드 작성

window.mainloop()   

from tkinter import *

window = Tk();                  # 윈도우(창, 스테이지,... 등)를 객체로 선언
window.geometry("500x300");     # 윈도우 창 크기 설정
window.title("계산기");         # 타이틀(제목) 설정
window.config(bg="skyblue");    # 배경 색상 설정
window.resizable(width=True, height=False);      # 창 크기 고정 여부(True-움직임, False-움직이지 않음)

window.mainloop();              # 창을 띄우는것(마지막에 항상 들어가는 코드)
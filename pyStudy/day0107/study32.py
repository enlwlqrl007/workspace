# 메시지상자(주사위 - 입력값을 받아 나타내기)
import tkinter as tk
from tkinter import simpledialog
import random

window = tk.Tk()
window.title('표준 입력 대화 상자2')
window.geometry('300x150')

comDice = random.randint(1,6)
manDice = simpledialog.askinteger('주사위 예축', '주사위 숫자를 입력하세요.', minvalue=1, maxvalue=6)

resStr = '컴퓨터 주사위 : ' + str(comDice) + '\n'
resStr += '사람의 예측값 : ' + str(manDice) + '\n'
resStr += '게임 결과 : ' 

if(comDice == manDice):
    resStr += '정확히 맞춤'
elif(comDice % 2 == 0 and manDice % 2 == 0):
    resStr += '짝수값 일치'
elif(comDice % 2 == 1 and manDice % 2 == 1):
    resStr += '홀수값 일치'
else:
    resStr += '예측 완전 실패'

label = tk.Label(window, text=resStr)
label.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)

window.mainloop()
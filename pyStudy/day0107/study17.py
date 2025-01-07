# 키보드 이벤트(엔터키로 대소문자 변환 후, entry1의 값을 entry2로 보내기)
import tkinter as tk

def pressKey(event):
    key = event.keycode
    if(key==13):
        str1 = entryStr1.get()
        str2 = ''
        for ch in str1:
            if(ch.isupper()): # 대문자를 소문자로
                ch = ch.lower()
            elif(ch.islower()): # 소문자를 대문자로
                ch = ch.upper()
            str2 += ch
        entryStr2.set(str2)

window = tk.Tk()
window.title('키보드 이벤트5')
window.geometry('150x150')

entryStr1 = tk.StringVar()
entry1 = tk.Entry(window, textvariable=entryStr1)
entry1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)
entry1.bind('<Key>', pressKey)

entryStr2 = tk.StringVar()
entry2 = tk.Entry(window, textvariable=entryStr2)
entry2.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

window.mainloop()
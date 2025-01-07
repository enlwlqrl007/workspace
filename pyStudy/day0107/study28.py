# 메뉴만들기(메뉴로 이미지 바꾸기)
import tkinter as tk

def pet_select(filename):
    photo = tk.PhotoImage(file="day0103/gif/" + filename)
    button.configure(image=photo)
    button.image = photo

window = tk.Tk()
window.title('메뉴7')
window.geometry('400x400')

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

photo = tk.PhotoImage(file='day0103\gif\호랑이.gif')
button = tk.Button(window, image=photo)
button.pack(expand=1, anchor=tk.CENTER, side=tk.LEFT)

petMenu = tk.Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='동물 선택', menu=petMenu)
petMenu.add_command(label='강아지', command=lambda:pet_select('강아지.gif'))
petMenu.add_command(label='고양이', command=lambda:pet_select('키키.gif'))
petMenu.add_command(label='호랑이', command=lambda:pet_select('호랑이.gif'))
petMenu.add_command(label='사자', command=lambda:pet_select('사자.gif'))
petMenu.add_command(label='여우', command=lambda:pet_select('여우.gif'))


window.mainloop()
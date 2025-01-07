# 탭(이미지 넣기)
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('탭 위젯2')

tabControl = ttk.Notebook(window)

tabDog = ttk.Frame(tabControl)
tabControl.add(tabDog, text='강아지')
tabCat = ttk.Frame(tabControl)
tabControl.add(tabCat, text='고양이')
tabFox = ttk.Frame(tabControl)
tabControl.add(tabFox, text='여우')
tabTiger = ttk.Frame(tabControl)
tabControl.add(tabTiger, text='호랑이')
tabLion = ttk.Frame(tabControl)
tabControl.add(tabLion, text='사자')

tabControl.pack(expand=1, fill='both')

photoDog = tk.PhotoImage(file='day0103\gif\강아지.gif')
labelDog = ttk.Label(tabDog, image=photoDog)
labelDog.pack()

photoCat = tk.PhotoImage(file='day0103\gif\키키.gif')
labelCat = ttk.Label(tabCat, image=photoCat)
labelCat.pack()

photoFox = tk.PhotoImage(file='day0103\gif\여우.gif')
labelFox = ttk.Label(tabFox, image=photoFox)
labelFox.pack()

photoTiger = tk.PhotoImage(file='day0103\gif\호랑이.gif')
labelTiger = ttk.Label(tabTiger, image=photoTiger)
labelTiger.pack()

photoLion = tk.PhotoImage(file='day0103\gif\사자.gif')
labelLion = ttk.Label(tabLion, image=photoLion)
labelLion.pack()

window.mainloop()
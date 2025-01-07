# 서브 윈도우 창2
import tkinter as tk

def openSubWindow():
    def close_sub():
        label1.configure(text=sub_entry1.get())
        label2.configure(text=sub_entry2.get())
        sub.destroy()

    sub = tk.Toplevel(window)
    sub.geometry('200x100+100+100')
    sub.title('서브 윈도우창')
    sub.grab_set()

    sub_entry1 = tk.Entry(sub)
    sub_entry1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)
    sub_entry2 = tk.Entry(sub)
    sub_entry2.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)
    sub_button = tk.Button(sub, text='확인', command=close_sub)
    sub_button.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

window = tk.Tk()
window.title('메인 윈도우창')
window.geometry('300x300')

button = tk.Button(window, text='서브 윈도우 열기', command=openSubWindow)
button.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

label1 = tk.Label(window, text='전달값1', font=('궁서체',18), fg='red')
label1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)
label2 = tk.Label(window, text='전달값2', font=('맑은고딕',18), fg='blue')
label2.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

window.mainloop()
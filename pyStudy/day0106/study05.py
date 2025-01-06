import tkinter as tk
import sqlite3

def insert_data():
    global edt1, edt2, edt3, edt4
    con = sqlite3.connect("guiDB")
    cur = con.cursor()
    # INSERT INTO userTable VALUES("kim", "김영삼", "kim03@naver.com", 1948)
    sql = "INSERT INTO userTable VALUES('"
    sql += edt1.get() + "','"
    sql += edt2.get() + "','"
    sql += edt3.get() + "',"
    sql += edt4.get() + ")"
    cur.execute(sql)
    con.commit()
    con.close()

window = tk.Tk()
window.geometry("500x200")

edt1 = tk.Entry(window, width=10)
edt1.pack(side = tk.LEFT, padx=10, pady=10)

edt2 = tk.Entry(window, width=10)
edt2.pack(side = tk.LEFT, padx=10, pady=10)

edt3 = tk.Entry(window, width=10)
edt3.pack(side = tk.LEFT, padx=10, pady=10)

edt4 = tk.Entry(window, width=10)
edt4.pack(side = tk.LEFT, padx=10, pady=10)

button1 = tk.Button(window, text="입력", command=insert_data)
button1.pack(anchor=tk.CENTER, side=tk.TOP, expand=1)


window.mainloop()
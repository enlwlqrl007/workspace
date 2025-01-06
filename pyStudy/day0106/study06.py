import tkinter as tk
import sqlite3

def select_data():
    con = sqlite3.connect("guiDB")
    cur = con.cursor()
    sql = "SELECT * FROM userTable"
    cur.execute(sql)
    for row in cur.fetchall():
        listbox1.insert(tk.END, row)
    con.close()


window = tk.Tk()
window.geometry("300x300")

button1 = tk.Button(window, text="조회", command=select_data)
button1.pack(anchor=tk.CENTER, side=tk.TOP, expand=1)

listbox1 = tk.Listbox(window, bg="yellow")
listbox1.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

window.mainloop()
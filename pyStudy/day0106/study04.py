import tkinter as tk

def insert_data():
    listbox1.insert(tk.END, entry1.get())

def delete_all():
    listbox1.delete(0, listbox1.size()-1)


window = tk.Tk()
window.geometry("200x400")

entry1 = tk.Entry(window, width=10)
entry1.pack(anchor=tk.CENTER, padx=10, pady=10)

button1 = tk.Button(window, text="입력", command=insert_data)
button1.pack(anchor=tk.CENTER, side=tk.TOP, expand=1)

button2 = tk.Button(window, text="모두지우기", command=delete_all)
button2.pack(anchor=tk.CENTER, side=tk.TOP, expand=1)

listbox1 = tk.Listbox(window, bg="yellow")
listbox1.pack(side=tk.BOTTOM, expand=1)




window.mainloop()
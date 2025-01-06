import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

frame1 = tk.Frame(window,bg="green")
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

frame2 = tk.Frame(window,bg="yellow")
frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=2)

window.mainloop()
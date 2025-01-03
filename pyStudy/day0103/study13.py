import tkinter as tk

def click_prev():
    global index;
    index -= 1;
    if(index < 0):
        index = len(fileList) -1
    photo = tk.PhotoImage(file=fileList[index]);
    imageLabel.configure(image=photo);
    imageLabel.image = photo;


def click_next():
    global index;
    index += 1;
    if(index >= len(fileList)):
        index = 0
    photo = tk.PhotoImage(file=fileList[index]);
    imageLabel.configure(image=photo);
    imageLabel.image = photo;

fileList = ["day0103/gif/cat.PNG","day0103/gif/dog.PNG","day0103/gif/mini.PNG","day0103/gif/tg.PNG","day0103/gif/rhdfyd.PNG"];
index = 0;

window = tk.Tk()
window.title("동물앨범 App");

btnPrev = tk.Button(window, text="<< Prev", command=click_prev);
btnNext = tk.Button(window, text=">> Next", command=click_next);

btnPrev.pack();
btnNext.pack();

photo = tk.PhotoImage(file=fileList[index]);
imageLabel = tk.Label(window, image=photo);
imageLabel.pack();

window.mainloop()
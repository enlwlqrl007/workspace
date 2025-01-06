import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox

# 데이터 입력
def insertData():
    con, cur = None, None;
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""

    con = sqlite3.connect("guiDB")
    cur = con.cursor()

    data1 = edt1.get();
    data2 = edt2.get();
    data3 = edt3.get();
    data4 = edt4.get();

    if data1 == "":
        messagebox.showwarning("경고", "ID를 입력하세요")
        return

    try:
        # ID중복 확인
        cur.execute("SELECT id FROM userTable WHERE id=?",(data1,))
        row = cur.fetchone()
        if row:
            messagebox.showwarning("경고", "이미 존재하는 ID입니다.")
            return

        # INSERT INTO userTable VALUES("no","노태우","noto@naver.com",1930)
        sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
        cur.execute(sql)
    except Exception as e:
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
    else:
        messagebox.showinfo("성공", "데이터 입력 성공!!")
    finally:
        con.commit()
        con.close()

# 데이터 조회
def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    con = sqlite3.connect("guiDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")
    strData1.append("사용자ID")
    strData2.append("사용자이름")
    strData3.append("이메일")
    strData4.append("출생연도")
    strData1.append("-"*10)
    strData2.append("-"*10)
    strData3.append("-"*10)
    strData4.append("-"*10)
    
    while(True):
        row = cur.fetchone()
        if row == None:
            break;
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(row[2])
        strData4.append(row[3])
    listData1.delete(0, listData1.size()-1)
    listData2.delete(0, listData2.size()-1)
    listData3.delete(0, listData3.size()-1)
    listData4.delete(0, listData4.size()-1)

    # listData1.delete(0, END)
    # listData2.delete(0, END)
    # listData3.delete(0, END)
    # listData4.delete(0, END)


    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
    con.close()

# 데이터 삭제
def deleteData():
    con, cur = None, None
    data1 = ""  # ID 저장할 변수
    sql = ""

    con = sqlite3.connect("guiDB")
    cur = con.cursor()

    data1 = edt1.get()  # 삭제할 ID받기

    if data1 == "":
        messagebox.showwarning("경고", "삭제할 ID를 입력하세요")
        return
    
    try:
        # DELETE FROM userTable Where id="data1";
        sql = "DELETE FROM userTable WHERE id='" + data1 + "'"
        cur.execute(sql)
        if(cur.rowcount) == 0:  # 삭제할 행이(정보) 없으면
            messagebox.showinfo("정보", "해당 ID가 존재하지 않습니다.")
        else:
            messagebox.showinfo("성공", "데이터 삭제를 완료했습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"데이터 삭제 오류:{e}")
    finally:
        con.commit()
        con.close()

window = tk.Tk()
window.geometry("600x300")
window.title("파이썬프로그래밍-송정빈")

edtFrame = Frame(window)
edtFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edt1 = Entry(edtFrame, width=10,); edt1.pack(side=tk.LEFT, padx=10, pady= 10)
edt2 = Entry(edtFrame, width=10,); edt2.pack(side=tk.LEFT, padx=10, pady= 10)
edt3 = Entry(edtFrame, width=10,); edt3.pack(side=tk.LEFT, padx=10, pady= 10)
edt4 = Entry(edtFrame, width=10,); edt4.pack(side=tk.LEFT, padx=10, pady= 10)

btnInsert = Button(edtFrame, text="입력", command=insertData, bg="#cddafd")
btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect = Button(edtFrame, text="조회", command=selectData, bg="#f1ddff")
btnSelect.pack(side=LEFT, padx=10, pady=10)
btnDelete = Button(edtFrame, text="삭제", command=deleteData, bg="#bee1e5")
btnDelete.pack(side=LEFT, padx=10, pady=10)

# 리스트 박스
listData1 = Listbox(listFrame, bg="#fff1e6"); listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg="#fff1e6"); listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg="#fff1e6"); listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg="#fff1e6"); listData4.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox

# 텍스트 있을때 placeholeder
def focus_in(event, entry, placeholeder, var):
    if var.get() == placeholeder:
        var.set("")
        entry.config(fg="black")

# 텍스트 비어있을때 placeholeder
def focus_out(event, entry, placeholeder, var):
    if var.get() == "":
        var.set(placeholeder)
        entry.config(fg="gray")

# 데이터 입력
def insert_Data():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""     # 사용자 입력 데이터 저장 변수
    sql = ""

    # SQLite 데이터베이스 연결
    con = sqlite3.connect("guiDB")
    cur = con.cursor()
    
    # 사용자입력 데이터 가져옴
    data1 = edt1.get()      # id
    data2 = edt2.get()      # 이름
    data3 = edt3.get()      # 이메일
    data4 = edt4.get()      # 출생연도

    # ID를 입력하지않고 버튼 누를시
    if data1 == "":
        messagebox.showwarning("경고", "ID를 입력하세요")
        return
    
    if not data4.isdigit():
        messagebox.showwarning("경고", "출생연도는 숫자만 입력 가능합니다.")
        return

    try:
        # ID 중복확인
        cur.execute("SELECT id FROM userTable WHERE id=?",(data1,))
        row = cur.fetchone()
        if row:
            messagebox.showwarning("경고", "이미 존재하는 ID입니다.")
            return
        
        # 예시문 : INSERT INTO userTable VALUES("sjb007", "송정빈", "sjb007@naver.com", 1996)
        sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")" 
        cur.execute(sql)
    except Exception as e:
        messagebox.showerror("오류","데이터 입력 오류가 발생")
    else:
        messagebox.showinfo("성공","데이터 입력 성공!!")
    finally:
        con.commit()
        con.close()


# 데이터 조회
def select_all():
    strData1, strData2, strData3, strData4, = [], [], [], []

    con = sqlite3.connect("guiDB")  
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")      #   테이블 데이터 전체 조회

    # 헤더추가
    strData1.append("사용자ID"); strData1.append("-" * 10)
    strData2.append("사용자이름"); strData2.append("-" * 10)
    strData3.append("이메일"); strData3.append("-" * 10)
    strData4.append("출생연도"); strData4.append("-" * 10)

    while(True):
        row = cur.fetchone()        # 한 행씩 가져오기
        if row == None:
            break
        data_exists = True          # 데이터가 있음을 표시
        strData1.append(row[0])     # 사용자 ID
        strData2.append(row[1])     # 사용자 이름
        strData3.append(row[2])     # 이메일
        strData4.append(row[3])     # 출생 연도

    # 데이터가 없으면 메시지 출력 후 종료
    if not data_exists:
        messagebox.showinfo("정보", "조회할 데이터가 없습니다.")
        con.close()
        return

    # 리스트박스 초기화
    listIdData.delete(0, END)
    listNameData.delete(0, END)
    listEmailData.delete(0, END)
    listBirthYearData.delete(0, END)

    # 리스트박스에 데이터 삽입
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listIdData.insert(END, item1)
        listNameData.insert(END, item2)
        listEmailData.insert(END, item3)
        listBirthYearData.insert(END, item4)
    
    con.close()


# 데이터 삭제(ID 검색)
def delete_Data():
    con, cur = None, None
    data1 = ""  # ID 저장 변수
    sql = ""

    con = sqlite3.connect("guiDB")
    cur = con.cursor()

    data1 = edt1.get()  # 삭제할 ID 입력값 가져오기

    if data1 == "":
        messagebox.showwarning("경고", "삭제할 ID를 입력하세요")
        return
    
    try:
        # 예시문 : DELETE FROM userTable WHERE id="data1";
        sql = "DELETE FROM userTable WHERE id='" + data1 + "'"
        cur.execute(sql)
        if(cur.rowcount) == 0:      # 삭제할 행(정보)이 없다면
            messagebox.showinfo("정보", "해당 ID가 존재하지 않습니다.")
        else:
            messagebox.showinfo("성공","데이터 삭제를 완료했습니다.")
    except Exception as e:
        messagebox.showerror("오류",f"데이터 삭제 오류:{e}")
    finally:
        con.commit()
        con.close()

window = tk.Tk()
window.geometry("750x300")
window.title("실버케어 데이터 관리_송정빈")

# 입력창 프레임
edtFrame = Frame(window)
edtFrame.pack()

# 리스트박스,스크롤바 프레임
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

# 스크롤바
scrollbar = Scrollbar(listFrame)
scrollbar.pack(side="right", fill="y")

# placeholder 텍스트
placeholder_id = "ID를 입력하세요"
placeholder_name = "이름을 입력하세요"
placeholder_email = "이메일을 입력하세요"
placeholder_birth_year = "출생연도를 입력하세요"

# StringVar를 사용하여 텍스트를 관리
var1 = tk.StringVar(value=placeholder_id)
var2 = tk.StringVar(value=placeholder_name)
var3 = tk.StringVar(value=placeholder_email)
var4 = tk.StringVar(value=placeholder_birth_year)

# ID 입력창
edt1 = Entry(edtFrame, width=15, textvariable=var1, fg='grey')      
edt1.pack(side=tk.LEFT, padx=10, pady=10)
edt1.bind("<FocusIn>", lambda event: focus_in(event, edt1, placeholder_id, var1))
edt1.bind("<FocusOut>", lambda event: focus_out(event, edt1, placeholder_id, var1))     

# 이름 입력창
edt2 = Entry(edtFrame, width=15, textvariable=var2, fg='grey')      
edt2.pack(side=tk.LEFT, padx=10, pady=10)
edt2.bind("<FocusIn>", lambda event: focus_in(event, edt2, placeholder_name, var2))
edt2.bind("<FocusOut>", lambda event: focus_out(event, edt2, placeholder_name, var2))  

# 이메일 입력창
edt3 = Entry(edtFrame, width=15, textvariable=var3, fg='grey')      
edt3.pack(side=tk.LEFT, padx=10, pady=10)
edt3.bind("<FocusIn>", lambda event: focus_in(event, edt3, placeholder_email, var3))
edt3.bind("<FocusOut>", lambda event: focus_out(event, edt3, placeholder_email, var3))  

# 출생연도 입력창
edt4 = Entry(edtFrame, width=15, textvariable=var4, fg='grey')      
edt4.pack(side=tk.LEFT, padx=10, pady=10)
edt4.bind("<FocusIn>", lambda event: focus_in(event, edt4, placeholder_birth_year, var4))
edt4.bind("<FocusOut>", lambda event: focus_out(event, edt4, placeholder_birth_year, var4))

# edtFrame 버튼
btnInsert = Button(edtFrame, text="입력", command=insert_Data, bg="#cddafd",)    # 입력버튼
btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect = Button(edtFrame, text="조회", command=select_all, bg="#f1ddff")     # 조회버튼
btnSelect.pack(side=LEFT, padx=10, pady=10)
btnDelete = Button(edtFrame, text="삭제", command=delete_Data, bg="#bee1e5")    # 삭제버튼
btnDelete.pack(side=LEFT, padx=10, pady=10)

# 리스트 박스
listIdData = Listbox(listFrame, bg="#fff1e6", yscrollcommand=scrollbar.set);          # id정보
listIdData.pack(side=LEFT, fill=BOTH, expand=1)    
listNameData = Listbox(listFrame, bg="#fff1e6", yscrollcommand=scrollbar.set);        # 이름 정보
listNameData.pack(side=LEFT, fill=BOTH, expand=1)    
listEmailData = Listbox(listFrame, bg="#fff1e6", yscrollcommand=scrollbar.set);       # 이메일 정보
listEmailData.pack(side=LEFT, fill=BOTH, expand=1)    
listBirthYearData = Listbox(listFrame, bg="#fff1e6", yscrollcommand=scrollbar.set);   # 출생연도 정보
listBirthYearData.pack(side=LEFT, fill=BOTH, expand=1)    

# 스크롤바 동작 설정
scrollbar.config(command=lambda *args: [listIdData.yview(*args), 
                                        listNameData.yview(*args), 
                                        listEmailData.yview(*args), 
                                        listBirthYearData.yview(*args)])

window.mainloop()
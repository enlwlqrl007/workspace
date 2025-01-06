import sqlite3

con = sqlite3.connect('guiDB')
cur = con.cursor()

while(True):
    data1 = input('사용자 ID --> ')
    if data1 == '':
        break;
    data2 = input('사용자 이름 --> ')
    data3 = input('이메일 --> ')
    data4 = input('출생연도 --> ')
    # INSERT INTO userTable VALUES("abc", "윤석열","abc@naver.com",1960)
    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")";
    cur.execute(sql)    # execute 요청

con.commit()
con.close()
import sqlite3

con = sqlite3.connect('guiDB')
cur = con.cursor()

# SELECT * FROM userTable
cur.execute("SELECT * FROM userTable")
print("사용자ID\t사용자이름\t이메일\t\t\t출생연도")
print("-"*70);

while(True):
    row = cur.fetchone()      # 커서의 위치 맨위
    if row == None:
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print(data1 + "\t\t" + data2 + "\t\t" + data3 + "\t\t" + str(data4))



con.close()
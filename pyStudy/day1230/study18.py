# 파일을 쓰기 모드로 열어 내용 작성

f = open("새파일.txt","w",encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다.\n"%i
    f.write(data);
f.close();

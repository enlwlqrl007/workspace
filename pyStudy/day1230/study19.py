# readline 함수 이용해서 파일 읽기

f = open("새파일.txt","r",encoding="UTF-8");
line = f.readline();
print(line)
line = f.readline();
print(line)
line = f.readline();
print(line)

f.close()


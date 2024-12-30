# read함수로 파일 읽기

f = open("새파일.txt", "r",encoding="UTF-8");
data = f.read();
print(data);
f.close()
print(type(data))
# 파일 객체를 for문과 함께 사용

f = open("새파일.txt", "r",encoding="UTF-8");
for line in f:
    print(line,end="");
f.close();
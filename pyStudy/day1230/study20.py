# readlines 함수 이용해서 파일 읽기

f = open("새파일.txt","r",encoding="UTF-8");
lines = f.readlines();
for line in lines:
    print(line,end="")  # 1번째 방법

    # line = line.strip() # 2번째 방법 줄 끝의 줄 바꿈 문자를 제거
    # print(line)

f.close()
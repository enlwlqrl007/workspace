# try - finally 문

try:
    f = open("error.txt","w");
    str = f.read();
    print("오류 없음");
finally:            # 중간에 오류가 발생해도 무좋건 실행함
    print("오류 있음");
    f.close();  
# 오류 회피하기

try:
    f = open("없는파일.txt","r")
except FileNotFoundError:   # 파일이 없더라도 pass 문구 하나로 오류가 생기더라도 통과됨
    pass

print("hello");
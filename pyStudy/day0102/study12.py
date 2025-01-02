# 여러개 오류 처리

try:
    a = [1,2]
    print(a[3])
    4 / 0 ;
except ZeroDivisionError as e:
    print(e)
    print("0으로 나눌 수 없습니다.");
except IndexError as e:
    print(e)
    print("인덱싱 할 수 없습니다.");
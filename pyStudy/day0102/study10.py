# 예외처리 : 오류가 발생할 때 실행되는 로직

# 자바에선 : try{}catch{}
# 파이썬에서 : try: except 에러이름 as e:

try:
    4 / 0
except ZeroDivisionError as e :
    print(e);


#format 함수를 사용한 포매팅
print("I eat {0} apples".format(3));

print("I eat {0} apples".format("five"));

num = 7;
print("I eat {0} apples".format(num));

# 인덱스 방식
print("나는 {0}개의 호빵을 먹었다. 그리고 {1}일 동안 배탈이 났다.".format(num,2));
# 이름으로 넣는 방식
print("나는 {number}개의 호빵을 먹었다. 그리고 {day}일 동안 배탈이 났다.".format(number=10, day=3));

# 인덱스 + 이름을 혼용하는 방식 -> 잘 사용하지 않음
print("나는 {0}개의 호빵을 먹었다. 그리고 {day}일 동안 배탈이 났다.".format(4, day=2));

# 왼쪽 정렬
print("{0:<10}원".format(100));

# 오른쪽 정렬
print("{0:>10}원".format(100));

# 가운데 정렬
print("{0:^10}원".format(100));

# 공백채우기
print("{0:-^10}원".format(100));
print("{0:!^10}원".format(100));

# 소수점표현
pi = 3.141592145
print("{0:0.4f}".format(pi));
print("{0:10.4f}".format(pi));

# {,} 문자를 표현
print("{{와}}".format());
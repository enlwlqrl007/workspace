from copy import copy

# 변수 - 값을 저장하는 공간
a = [1,2,3];
print(id(a));   # 값이 저장 되어 있는 주소를 반환

# 리스트 복사
b = a   # 값의 주소를 복사한 것,
print(b);
print(id(a)," ",id(b));

a[2] = 4;
print(a);
print(b);

# [:] 이용 - 이걸 많이 사용!
a=[1,2,3];
b= a[:];    
a[1] = 4;
print(a);
print(b);
print(id(a)," ",id(b));

# copy 모듈 사용
c = [1,2,3]
d = copy(c);
print(c);
print(d);
print(id(c)," ",id(d));
# 리스트 연산

a = [1,2,3];
b = [4,5,6];

print(a+b);
print(a*3);
print(len(a));

print(str(a[2])+ "dog");

# 리스트의 수정과 삭제
a[2] = 4;
print(a);

# 리스트 요소 삭제
del a[1];
print(a);

a = [1,2,3,4,5,6,7,8,9,10];
del a[5:];
print(a);
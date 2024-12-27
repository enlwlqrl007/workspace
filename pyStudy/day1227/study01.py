# 리스트

a = [1, 3, 5, 7, 9];
b = [];
c = ['Life', 'is', 'too', 'short'];
d = [1, 2, 'Life', 'is'];
e = [1, 2, ['Life', 'is']];

print(c[2]);
print(e[2][0]);

# 리스트 인덱싱
print(a[-2]);
print(e[-1]);
print(e[-1][1]);

# 리스트 슬라이싱
a = [1,2,3,4,5];
print(a[0:2]);
print(a[:3]);
print(a[3:]);
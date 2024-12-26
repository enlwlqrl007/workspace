# 문자열 인덱싱, 슬라이싱

a = "Life is too short, You need Python";
print(a[3]);
print(a[-2]); # 뒤에서부터 인덱스 -1로 시작

# 슬라이싱
print(a[0:4]);
print(a[19:]);
print(a[:19]);

str = "20241226Sunny";
date = str[:8];
weather = str[8:];
print(date);
print(weather);
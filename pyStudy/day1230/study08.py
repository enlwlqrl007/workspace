a = [1,2,3,4];
result = [];

for num in a:
    result.append(num*3);
print(result);

# 리스트 컴프리핸션
result = []
result = [num*3 for num in a]
print(result);

# 리스트 a에서 짝수에만 3을 곱하기
result = [];
result = [num*3 for num in a if num % 2 == 0]
print(result);

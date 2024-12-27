#집합 자료형
s1 = set([1,2,3]);
print(s1);

s2 = set('apple')   # 집합자료형은 중복된 값은 하나만 나타나고, 순서도 없다.
print(s2);

l1 = list(s1);
print(l1);

t1 = tuple(s1);
print(t1);

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6]);
s2 = set([4,5,6,7,8,9]);

# 교집합
print(s1 & s2);
print(s1.intersection(s2));

# 합집합
print(s1|s2);
print(s1.union(s2));

# 차집합
print(s1-s2);
print(s1.difference(s2));

# 집합자료형 관련 함수
# 값 1개 추가하기
s1 = set([1,2,3]);
s1.add(4);
print(s1);

# 값 여러개 추가하기
s1.update([5,6,7,8,9,10]);
print(s1);

# 특정 값 제거
s1.remove(3);
print(s1);


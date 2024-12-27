# 리스트 관련 함수

# 추가하기
a = [1,2,3];
a.append(4);
print(a);
a.append([5,6,7]);
print(a);

# 리스트 정렬(sort)
a = [1,4,3,2];
a.sort()                # 오름차순
print(a);
a.sort(reverse=True)    # 내림차순
print(a)

str = ['a','c','b'];
print(str);
str.sort();
print(str);

# 리스트 정렬(reverse) - 뒤집기
a = ['a','c','b','e'];
a.reverse();
print(a);

# 인덱스 반환
a = [1,2,3];
print(a.index(2));

# 리스트 요소 삽입
a = [1,2,3,4];
a.insert(1,4);
print(a);

# 리스트 요소 제거
a = [1,2,3,1,2,3];
a.remove(3);
print(a);

# pop() - 맨 마지막 인덱스 위치의 값을 리스트에서 빼낸다.
a = [1,2,3];
print(a.pop());
print(a);

b = [1,2,3,4,5];
print(b.pop(1)); # 1 => 인덱스번호
print(b);

# count() - 리스트에 포함된 특정 요소의 갯수 카운트
a = [1,2,3,1];
print(a.count(1));

# extend - 리스트의 확장 
a = [1,2,3];
a.extend([4,5]);
print(a);
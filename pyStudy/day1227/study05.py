# 딕셔너리 자료형
dic={'name':'윤석열','phone':'010-1234-5678','birth':'1227'};
print(dic);
print(dic['name']);

# 딕셔너리 쌍 추가하기
a = {1:'a'};
a[2] = 'b';
print(a);
a['name']='문재인';
print(a);
a[3] = [1,2,3];
print(a);

# 딕셔너리 요소 삭제
del a[3];
print(a);

grade = {'국어':90,'영어':80,'수학':100};
print(grade['영어']);

# 딕셔너리 주의점!
a = {1:'a',1:'b'};  # 같은 인덱스 위치에 중복으로 값을 넣으면 뒤에 값만 인정됨!
print(a);

# a = {[1,2]:'hi'};     # 키 값은 리스트가 될 수 없다.
# print(a);

# 딕셔너리 관련 함수
a = {'name':'박근혜','phone':'010-1111-2222','birth':'1228'};
print(a.keys());        # a 딕셔너리의 키값만 불러오기

for k in a.keys():
    print(k);

print(list(a.keys()));  # 리스트 형식으로 불러오는 방법

# value 리스트 만들기
print(a.values());      # a 딕셔너리의 벨류값만 불러오기
print(list(a.values()));

# key,value 의 쌍을 얻는방법 - items()
print(a.items());

# key,value 를 모두 지우는방법 - clear()
a.clear();
print(a);

# key로 value를 얻기 - get();
a = {'name':'박근혜','phone':'010-1111-2222','birth':'1228'};
print(a.get('name'));
print(a['name']);

print(a.get('address'));
# print(a['address']);

# 해당 key가 딕셔너리에 있는지 조사
print('name' in a);
print('address' in a);
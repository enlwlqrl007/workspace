# 문자열 관련 함수

a = 'apple is red.';
print(a.count('p'));    # 해당 문자의 개수 세기
print(a.find('r'));     # 해당 문자의 인덱스 번호 확인 / 중복 문자일 경우 첫번째 문자의 인덱스 위치 반환

print(a.find('x'));     # -1 값은 없을 경우

print(a.index('e'));
# print(a.index('x'));    # find와 차이점 : 없는 문자를 찾을땐 에러가 생김

str = ','.join('abcd');     # join : 문자열 삽입
print(str)

a = 'hi';
print(a.upper());       # 소문자를 대문자로 봐꾸는 메서드

b = 'HI';
print(b.lower());       # 대문자를 소문자로 봐꾸는 메서드

name = " 윤석열 "
print(name);
print(name.lstrip());   # lstrip(): 왼쪽 공백을 지움
print(name.rstrip());   # rstrip(): 오른쪽 공백을 지움
print(name.strip());    # strip(): 왼쪽,오른쪽 공백 지움

str = 'Life is too short';
print(str.replace("Life","Your leg"));      # 문자열 변경

# 문자열 나누기
print(str.split());     # split(): 리스트 형태인 공백기준으로 나눠짐
b = "a:b:c:d";
print(b.split(':'));    

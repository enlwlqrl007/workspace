# 내장함수1

# abs : 절대값 반환
print(abs(-3));
print(abs(+3));

# all : 리스트 같은 반복 가능한 데이터에 모든 요소가 참이면 True를 반환
print(all([1,2,3]));
print(all([0,1,2,3]));
print([True, False]);

# any : 반복 가능한 데이터에 요소 중 하나라도 참이면 True 
print(any([1,2,3]));
print(any([0,1,2,3]));
print(any([True, False]));
print(any([False, False]));

# chr : 유니코드 숫자 값을 입력받아 문자를 리턴
print(chr(97));
print(chr(44032));

# dir : 객체가 지닌 변수나 함수를 보여준다.
a = [1,2,3];
print(dir(a));
s = "apple";
print(dir(s));
print(dir.__doc__); # doc 스트링 조회: 함수 설명 참조

# divmod : 2개 숫자를 입력받고, a를 b로 나눈 몫, 나머지 튜플
print(divmod(7, 3))

# enumerate :순서가 있는ㄷ ㅔ이터를 입력으로 받아 인덱스를 포함하는 enumerate객체를 리턴
for i, name in enumerate(["apple","banana","orange"]):
    print(i, name)

# eval : 문자열로 구성된 표현식을 입력으로 받아서 해당 문자열을 실행한 결과를 리턴
print(eval("1+2"));
print(eval("divmod(4,3)"));



# 내장함수2

# filter : 반복 가능한 자료의 각각의 요소의 참,거짓을 판별하여 선별하여 리턴한다.
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i);
    return result;

print(positive([1,-3,2,0,-5,6]));

def positive(x):
    return x > 0;

print(list(filter(positive, [1,-3,2,0,-5,6])));

# hex : 정수를 입력받아 16진수 문자열로 변환해서 리턴
print(hex(234));
print(type(hex(234)));

# id : 객체의 주소값을 리턴
a = 3; 
print(id(a));

# input : 사용자 키보드 입력을 받는 함수
# a = input();
# print(a);

# int : 문자열 형태의 숫자를 정수로 리턴
a = "3";
print(int(a) + 2);
print(int(3.14));
print(int("101",2));    # 2진수를 10진수로 변경하여 리턴
print(int("FFF",16));   # 16진수를 10진수로 변경하여 리턴

# isinstance : 입력받은(첫번째) 객체가 입력받은(두번째) 클래스의 객체인지 판단하여 true, false를 반환
class Person:
    pass
class Person2:
    pass
a = Person()
b = Person2()

print(isinstance(a, Person));
print(isinstance(b, Person));

# len : 요소의 전체 개수
print(len("Hi~ I am student"));

# list : 리스트로 만들어서 반환
print(list("python"));
print(list((1,2,3)));

# map : 입력받은 데이터의 각 요소에 함수를 적용한 결과를 리턴 함수
# -> map을 사용안했을 때 코드
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result;
result = two_times([1,2,3,4])
print(result)

# -> map을 사용했을때 코드
def two_times(x):
    return x * 2;
print(list(map(two_times, [1,2,3,4])));

# -> lambda 함수를 사용했을때 코드
print(list(map(lambda a: a*2,[1,2,3,4])));

# max, min : 최댓값, 최솟값
print(max([45,78,300,200]));
print(min([45,78,300,200]));

# oct : 8진수를 문자열로 반환
print(oct(60))

# open : 파일 열기

# ord : 문자의 유니코드 반환
print(ord('a'));

# pow : xfmf y제곱
print(pow(2, 3));

# range : for문과 자주 사용하는 범위 값을 반복 가능한 객체로 만들어 반환
print(list(range(5)));          # 1번째 인자만 있는 경우는 인덱스 5개까지의 리스트
print(list(range(1, 5)));       # 1번째 인자는 숫자시작 2번째 인자는 -1을 한 값까지 
print(list(range(1, 10, 2)));   # 3번째 인자는 숫자사이의 거리

# round : 반올림해서 리턴
print(round(4.6));
print(round(4.2));

# sorted : 정렬해서 리턴
print(sorted([4,1,3,2]));
print(sorted(['b','c','f','a']));
print(sorted("school"));

# str : 문자열로 변환해서 반환
print(str(5) + '2');

# sum : 합을 리턴
print(sum([1,2,3,4,5,6,7,8,9,10]));

# tuple : 튜플로 변환해서 반환
print(tuple([1,2,3,4,5,6,7,8,9,10]));

# type : 자료형을 반환
print(type(3));
print(type(3.14));
print(type('f'));

# zip : 동일한 개수로 이루어진 데이터들을 묶어서 리턴
print(list(zip([1,2,3],[4,5,6])));
print(list(zip([1,2,3],[4,5,6],[7,8,9])));
print(list(zip("abc","def")));
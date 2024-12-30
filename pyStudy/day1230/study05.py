# for문
# 기본구조
# for 변수 in 리스트(튜플,문자열...):
#   수행할_문장1
#   수행할_문장2
#   수행할_문장3

test_list = ['one','two','three'];
for i in test_list:
    print(i);

a = [(1,2),(3,4),(5,6)];
for (first, last) in a:
    print(first + last);

# 5명의 학생의 시험점수가 60점 이상이면 합격이고,
# 그렇지 않으면 불합격을 출력하는 결과를 보여주세요.
# 출력결과
# 1번 학생은 합격입니다.
# 2번 학생은 불합격입니다. 

marks = [90, 25, 67, 45 ,80];
number = 0;
for mark in marks:
    number += 1;
    if mark >= 60:
        print("%d번 학생은 합격입니다."%number);
    else:
        print("%d번 학생은 불합격입니다."%number);

number = 0; flagStr = "";
for mark in marks:
    number += 1;
    print("%d번 학생은 %s입니다."%(number,'합격'if mark >= 60 else "불합격"));

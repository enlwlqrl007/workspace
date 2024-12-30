# and, or, not

# 논리연산
# x or y : x와 y 중 하나 이상이 참인 경우
# x and y : x와 y가 모두 참인 경우
# not x : x가 참이면 거짓, 거짓이면 참을 반환

money = 2000;
card = True;
if money >= 4800 or card:
    print("택시를 탄다.")
else:
    print("걸어간다.")

gender = 'man';
age = 20;
if gender == 'man' and age == 20:
    print("징병대상");
else:
    print("면제");

x = True
if not x:
    print("실행");
else:
    print("종료");

# in, not in
print(1 in [1,2,3]);    # True
print(4 in [1,2,3]);    # False

print(1 not in [1,2,3]);    # False
print(4 not in [1,2,3]);    # True

print("p" in "python");     # True
print("x" in "python");     # False

pocket = ["paper", "cellphone", "money"]
if "money" in pocket:
    print("택시를 탄다.");
else:
    print("걸어간다.");

if "money" in pocket:
    pass
else:
    print("걸어간다.");

# elif
pocket = ["paper", "cellphone"]
card = True;
if "money" in pocket:
    print("택시를 탄다.");
elif card:
    print("택시를탄다.");
else:
    print("걸어간다.");

# else:
#     if card:
#         print("택시를 탄다.")
#     else:    
#         print("걸어간다.");

# if score >= 60:
#     message = "합격";
# else:
#     message = "불합격";

# 삼항연산자
score = 55;

message = "합격" if score >= 60 else "불합격";
print(message);

# score 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 c, 60점 이상이면 D, 아니면 F
score = 76;

if score >= 90:
    print("A");
elif score >= 80:
    print("B");
elif score >= 70:
    print("C");
elif score >= 60:
    print("D");
else:
    print("F");

# 스와핑 알고리즘
a = 7; b = 3;
print("a=",a);
print("b=",b);
print("스와핑 실행 후");
t = a;
a = b;
b = t;

print("a=",a);
print("b=",b);
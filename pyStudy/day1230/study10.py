# 함수

def mySum(x, y):
    """이 함수는 더하는 함수다."""  # doc 스트링 : 함수 설명서
    result = x + y;
    return result;

def returnHi():
    return "Hi~";


def sayHi():
    print("Hi~!");

num1 = 1;
num2 = 3;

s = mySum(num1, num2);
print(s);
sayHi();
print(returnHi());

print(mySum.__doc__);
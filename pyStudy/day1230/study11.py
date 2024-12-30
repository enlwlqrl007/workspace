# 입력값이 몇 개가 될지 모를 때

def add_many(*args):
    result = 0;
    for i in args:
        result += i;
    return result;

x = add_many(1,2,3);
print(x)

x = add_many(1,2,3,4,5,6,7,8,9,10);
print(x)

def add_mul(choice, *args):
    if choice == "add":
        result = 0;
        for i in args:
            result+= i;
    elif choice == "mul":
        result = 1;
        for i in args:
            result *= i;
    return result;


x = add_mul('add',1,2,3,4,5)
print(x);

x = add_mul('mul',1,2,3,4,5)
print(x);

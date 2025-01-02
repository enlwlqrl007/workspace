# 클래스

# result1 = 0;
# result2 = 0;

# def add1(num):   # 누산기
#     global result1;
#     result1 += num;
    
#     return result1;

# def add2(num):   # 누산기
#     global result2;
#     result2 += num;
    
#     return result2;

# print(add1(3));
# print(add1(4));

# print(add2(3));
# print(add2(7));

class Calculator:
    def __init__(self):
        self.result = 0;

    def add(self, num):   # 누산기
        self.result += num;

        return self.result;

cal1 = Calculator();
cal2 = Calculator();

print(cal1.add(3));
print(cal1.add(4));
print(cal2.add(3));
print(cal2.add(7));
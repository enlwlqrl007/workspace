# 사칙 연산 클래스
#               + , -  , * , /            입력받는 메서드
# 메서드가 4개(add, sub, mul, div) + 메서드 1개(setData)

class FourCal:

    def __init__(self, first, second):      # 생성자  -> 파이썬에서 이렇게 사용함
        self.first = first;
        self.second = second;

    def setData(self, first, second):
        self.first = first;
        self.second = second;

    def add(self):
        result = self.first + self.second;
        return result;

    def sub(self):
        result = self.first - self.second;
        return result;

    def mul(self):
        result = self.first * self.second;
        return result;

    def div(self):
        result = self.first / self.second;
        return result;


# a = FourCal();
# a.setData(4, 2);

a = FourCal(4,2);

print(a.add());     # 결과 6;   
print(a.sub());     # 결과 2;
print(a.mul());     # 결과 8;
print(a.div());     # 결과 2;
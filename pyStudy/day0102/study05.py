# 클래스 상속


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

# ()안에 부모 이름 넣으면 상속 됨!
class FiveCal(FourCal):
    def pow(self):
        result = self.first ** self.second;
        return result;

    # 부모에 있는 second가 0일때를 에러발생으로 인해 수정하고 싶을때
    def div(self):  # 오버라이드  (부모껄 재정의하다)
        if self.second == 0:
            return 0;
        else:
            result = self.first / self.second;
            return result;

a = FiveCal(4, 2);
print(a.pow());
print(a.add());

# 메서드 오버라이드 
# b = FourCal(4, 0);    -> FourCal에는 second가 0일때 에러발생처리 경우를 만들지 않아서 주석처리
# print(b.div());

print(a.div());
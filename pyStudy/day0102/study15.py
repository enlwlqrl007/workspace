# 오류 일부러 발생시키기    raise  명령어

class Bird:
    def fly(self):
        raise NotImplementedError;
    
class Eagle(Bird):
    def fly(self):  # 오버라이드 : 재정의
        print("very fast!!");

eagle = Eagle();
eagle.fly();
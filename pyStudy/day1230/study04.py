# while문 강제로 빠져 나가기.  break문

coffee = 10;
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.");
        coffee -= 1 # coffee = coffee -1   과 똑같다.
    elif money >= 300:
        print("거스름돈 %d원과 커피를 줍니다."%(money-300));
        coffee -= 1;
    else:
        print("돈을 돌려주고 커피를 주지 않습니다.");
        print("남은 커피는 %d잔입니다."%coffee);
    if coffee == 0:
        print("품절");
        break
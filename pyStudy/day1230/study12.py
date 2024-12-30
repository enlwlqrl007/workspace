# 매개변수에 초기값 미리 설정

def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다."%name);
    print("나이는 %d살 입니다."%age);
    
    if man:
        print("나는 남자입니다.");
    else:
        print("나는 여자입니다.");

say_myself("윤석열",62);
say_myself("김건희",58,False);
say_myself("문재인",67,True);

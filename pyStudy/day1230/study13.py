# 함수 안에서 선언한 변수의 효력 범위

a = 1;
def varTest1(a):
    a = a + 1;
    return a;

varTest1(a)
print(a);


a = 1;
def varTest2():
    global a 
    a = a + 1;
    

varTest2();
print(a);
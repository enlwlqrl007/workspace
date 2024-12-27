# boolean 자료형 - True, False
a = True;
b = False;

print(type(a));

print(1==1);
print(2==1);

l = [1,2,3,4];
while l:    # a가 참인 동안 실행, 1이 비었을때 false
    print(l.pop());

if [1,2,3]:
    print("참");        # 리스트에 값이 있을때
else:
    print("거짓");      # 리스트가 비어 없을때 

if():               
    print("참");        # 튜플 값이 있을때
else:
    print("거짓");      # 튜플이 비어 있을때


if None:               
    print("참");        # 튜플 값이 있을때
else:
    print("거짓");      # 튜플이 비어 있을때

# boolean 연산
print(bool('apple'));       # True
print(bool(''));            # False
print(bool([1,2,3]));       # True
print(bool([]));            # False


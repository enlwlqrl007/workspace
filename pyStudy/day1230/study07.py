# for 문과 함께 자주 쓰이는 range()함수


a = range(10)   # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a);

a = range(1,10) # 1, 2, 3, 4, 5, 6, 7, 8, 9 
print(a);

marks = [90, 25, 88, 77, 80]
for number in range(len(marks)): # range(5)랑 같음
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1));

for i in range(10, 100):
    print(i);

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %d"%(i,j,i * j))
    print();


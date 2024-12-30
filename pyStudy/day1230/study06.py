# for문과 continue문
# for문 안에서 continue문을 만나면 for문의 처음으로 돌아간다.
# break문은 루프를 탈출한다.
marks = [90, 25, 88, 77, 80]
number = 0;
for mark in marks:
    number += 1;
    if mark < 60:
        continue    
    print("%d번 학생 축하합니다."%number);
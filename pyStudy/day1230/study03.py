# while문

treeHit = 0;
while treeHit < 10:
    treeHit = treeHit+1
    print("나무를 %d번 찍었습니다."%treeHit);
    if treeHit == 10:
        print("나무가 넘어갑니다.");

propmt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
"""
number = 0;
while number != 4:
    print(propmt)
    number = int(input());


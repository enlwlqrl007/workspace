# 주소록 앱(파일 입출력 공부)
# 주소입력, 주소 개별조회, 주소전체조회, 삭제, 프로그램 종료

# 1. 주소입력
def saveData():
    name = input("이름: ");
    telNum = input("전화번호: ");
    addStr = input("주소: ");
    inputData = name + ", " + telNum + ", " + addStr + "\n";
    with open("addData.txt","a",encoding="UTF-8") as f:
        f.write(inputData);

# 주소 개별 조회
def selSeach():
    count = 0;
    key = input("검색할 이름: ")

    with open("addData.txt", "r", encoding="UTF-8") as f:
        data = f.readlines();       
    
    found = False
    for line in data:
        sub_data = line.strip().split(",");
        if sub_data[0] == key:
            count += 1;
            print("------------------------");
            print("이름:", sub_data[0]);
            print("전화번호:", sub_data[1]);
            print("주소:", sub_data[2]);
            print("------------------------");
            found = True;
            break;

    if not found:
        print("해당 이름이 존재하지 않습니다.");
    else:
        print(str(count)+ "명의 데이터를 조회했습니다.");

# 주소 전체 조회
def selTotal():
    count = 0;
    with open("addData.txt", "r", encoding="UTF-8") as f:
        data = f.readlines();
    print("------------------------");
    print("이름\t전화번호\t주소\t")
    print("------------------------");

    for line in data:
        sub_data = line.split(",");
        if len(sub_data) == 3:
            count += 1;
            print(sub_data[0]+"\t"+ sub_data[1]+"\t"+sub_data[2])     
    print(str(count)+ "명의 데이터를 조회했습니다.");

# 삭제
def delData():
    key = input("삭제할 이름: ");

    with open("addData.txt", "r", encoding="UTF-8") as f:
        data = f.readlines();

    found = False
    with open("addData.txt", "w", encoding="UTF-8") as f:
        for line in data:
            sub_data = line.strip().split(",");
            if sub_data[0] == key:  
                found = True
                print("삭제가 완료되었습니다.");
                continue  
            f.write(line);

    if not found:
        print("해당 이름이 존재하지 않습니다.");


while True:
    print("----------------");
    print("1. 주소 입력");
    print("2. 주소 개별조회");
    print("3. 주소 전체조회");
    print("4. 삭제");
    print("5. 프로그램 종료");
    print("----------------");
    op = input(">>");
    
    if op == "1":
        saveData();
    
    if op == "2":
        selSeach();

    if op == "3":
        selTotal();

    if op == "4":
        delData();

    if op == "5":
        break;

    else:
        print("잘못 입력하셨습니다.")
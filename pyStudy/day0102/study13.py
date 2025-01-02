# try - else문

try:
    age = int(input("나이를 입력하세요: "));
except:
    print("나이를 다시 입력하세요.");
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.");
    else:
        print("환영합니다.");
# f=open("test1.txt","w",)
# f.write("Hello FileProcessing\n");
# f.close();

# with구문 사용
with open("test1.txt","w",) as f:           # 블럭이 끝나는 순간 f가 자동으로 close된다.
    f.write("Hello FileProcessing!!!\n");
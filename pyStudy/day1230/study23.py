f = open("lottoData.CSV", "r",encoding="UTF-8");
data = f.read();
print(data)
f.close();

key = input("회차를 입력하세요: ")

subData = data.split("\n");

for i in range(1, len(subData)):
    subSubData = subData[i].split(",");
    if subSubData[0] == key:
        for j in range(1,len(subSubData)):
            print(subSubData[j], end=" ");
        




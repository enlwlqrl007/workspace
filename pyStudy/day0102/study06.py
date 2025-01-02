# 클래스 변수

class Family:
    lastName = "김";

a = Family()
b = Family()

print(Family.lastName);
print(a.lastName);
print(b.lastName);

Family.lastName = "박";
print(Family.lastName);
print(a.lastName);
print(b.lastName);

b.lastName = "최";
print(Family.lastName);
print(a.lastName);
print(b.lastName);
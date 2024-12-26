# f문자열 포맷팅

name = "홍길동";
age = 30;
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.");

print(f"내년에 나이는 {age + 1}입니다.");

d = {'name':'홍길동','age':30};
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.');

print(f'{"hi":<10}');
print(f'{"hi":>10}');
print(f'{"hi":^10}');
print(f'{"hi":-^10}');

y=3.141592;
print(f'{y:0.4f}');
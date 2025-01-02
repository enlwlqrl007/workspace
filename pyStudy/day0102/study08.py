# from 모듈이름 import 모듈함수

from mod1 import add
print(add(5,5));
# print(sub(5,5));      에러나는 이유 add함수만 가져와서 -> 사용하려면 1. from mod1 import add, sub     2. from mod1 import *   2번은 잘 안씀.(리소스 차지해서 무거움)

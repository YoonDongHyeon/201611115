#모듈은 함수의 집합
# import random as rn -> random을 이제 rn이라고 간략하게 쓸수 있다.
# from random import randint  -> randint만 가져온다. 그러면 random 중에 randint기능만 가져 온다.
# from random import randint as ri -> 라고 하면 ri로 코딩상에서 간략하게 쓸수 있다
#  그래서, 모듈을 한번 만들어 보자.
def myadd(a,b):
    return  a+b

def mysub(a,b):
    return  a-b
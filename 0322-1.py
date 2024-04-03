def sayHello(name):
    print("안녕하세요, %s씨." %(name))

def intro(myName, age):
    print("저는 {}세 {}입니다.".format(age, myName))

#매개변수를 얼마나 받을지 모를 때,
def myFruits(*fruits):
    for item in fruits:
        print("내가 좋아하는 과일은 {}입니다.".format(item))

#default값 지정
def intro2(myName="정진우", age=24):
    print("저는 {}세 {}입니다.".format(age, myName))


def max(a, b):
    if a > b:
        return a
    else:
        return b


def myDiv(a, b):
    q = a // b
    r = a % b
    return q, r
"""
sayHello("정진우")
intro("정진우", 24)
intro(age=20, myName="정진우")
myFruits("사과", "망고", "자몽")
intro2()
"""


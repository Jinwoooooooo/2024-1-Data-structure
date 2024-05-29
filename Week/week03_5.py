

def sayHello(name):
    print("안녕하세요, %s씨!"%(name))

def intro(myName="강감찬", age=20):
    print("저는 {}세, {}입니다.".format(age, myName))

def myFruits(*fruits):
    for item in fruits:
        print("나는 {}을 좋아합니다.".format(item))
            
def max(a, b):
    if a > b:
        return a
    else:
        return b

def myDiv(a, b):
    q = a // b
    r = a % b
    return q, r

print(myDiv(5,3))













"""
객체의 속성명, 메소드명을 차례대로 출력하는 함수 만들기
사용 예:
showObject(object):


a = []
showObject(a)

1: __add__
2: __class__
3 ...
4 ...
"""

def showObject(obj):
    count = 1
    for attr in dir(obj):
        print(f"{count}: {attr}")
        count+=1

a = []
showObject(a)

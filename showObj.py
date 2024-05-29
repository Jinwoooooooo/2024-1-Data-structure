"""
객체의 속성명, 메소드명을 차례대로 출력하는 함수 만들기
사용예:
showObject(obj):
    ....
    ....


a = []
showObject(a)

1: __add__
2: __class__
...
"""
def showObject(obj):
    # 객체 obj의 속성 리스트를 가져온다.
    lst = dir(obj)

    #lst에 저장된 항목값들을 순번과 함께 출력한다.
    count = 1
    for item in lst:
        print("%2d: %s"%(count, item))
        count += 1


    

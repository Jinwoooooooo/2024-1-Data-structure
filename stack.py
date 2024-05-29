#이중 연결리스트(dbllist)를 활용하여 stack을 구현한다.
from dbllist import *

# Stack Empty Error Class
class StackUnderFlow(Exception):
    pass


# Stack class 정의하기
class Stack(DList):
    # stack에 새 값을 추가한다. (DList.insertFront로 구현)
    def push(self, value):
        self.insertFront(value)

    # stack의 맨 위에 있는 값을 제거하면서 반환한다.
    def pop(self):
        if self.count == 0: # stack empty이면
            raise StackUnderFlow("Stack Empty!!!")
        else:
            returnValue = self.head.data;
            self.remove(self.head)
            return returnValue
    
    # stack empty 여부를 확인하여 True, False로 반환한다.
    # Empty이면 True, 아니면 False 반환.
    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    # stack의 top 값을 확인만 한다. (pop()과 다름.)    
    def peek(self):
        if self.isEmpty():
            raise StackUnderFlow("Stack Empty!!!")
        else:
            return self.head.data










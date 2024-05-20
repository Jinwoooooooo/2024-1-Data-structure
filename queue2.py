from dbllist import *

#=============================================
#Queue Empty Error Class
class QueueUnderFlow(Exception):
    pass

#=============================================
#이중 연결 리스트를 이용하여 Queue를 정의한다.
class Queue(DList):
    #Queue에 자료를 추가하는 연산
    def add(self, value):
        self.append(value)

    #Queue에서 자료를 하나 가져오는(삭제) 연산
    def remove(self):
        if self.isEmpty():
            raise QueueUnderFlow("Queue is Empty!")
        else:
            returnValue = self.head.data
            super().remove(self.head)   #Queue의 remove()가 아닌 DList의 remove()를 호출한다.
            return returnValue
    
    
        
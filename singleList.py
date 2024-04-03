#연결 리스트에 사용할 노드 객체 생성용 클래스를 먼저 정의

class Node:
    def __init__(self, data):
        self.data = data    #노드 생성하면서 넘겨준 값을 data 속성에 저장
        self.next = None    #노트 생성 순간에는 다음 노드가 없으므로, None

#생성된 Node 객체(인스턴드)들을 연결할 단순 연결 리스트(Singly Linked List) 객체 정의
class SList:
    def __init__(self):
        self.head = None    #단순 연결 리스트 생성 초기에는 노드가 없으므로 None
        self.count = 0

#===============================
sl = SList()
n = Node(100)
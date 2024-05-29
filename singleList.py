#연결 리스트에 사용할 노드(node) 객체 생성용 클래스를 먼저 정의
class Node:
    def __init__(self, data):
        self.data = data    #노드 생성하면서 넘겨준 값(data)을 data 속성에 저장
        self.next = None    #노드 생성 순간에는 다음 노드가 없으므로, None
    
    def __str__(self):  # print문과 같은 상황에서 객체를 나타낼 수 있는 문자열을 구성하여 반환.
        return f"[{self.data}]"

#생성된 Node 객체(인스턴드)들을 연결할 단순 연결 리스트(Singly Linked List) 객체 정의
class SList:
    #-----------------------------------------------------------------------------------
    def __init__(self):
        self.head = None    #단순 연결 리스트 생성 초기에는 노드가 없으므로 None
        self.count = 0
    #-----------------------------------------------------------------------------------
    def __str__(self):
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.data)
            current = current.next
        return str(lst)

    #-----------------------------------------------------------------------------------
    def remove(self, value):    # value값을 가진 노드를 리스트 연결에서 분리하여 반환한다.
        #value값을 가진 노드가 있는지 여부를 먼저 확인한다.
        targetNode = self.find(value)
        if targetNode is None:
            return None
        else:
            previous = None
            current = self.head
            while current is not targetNode:
                previous = current
                current = current.next

            # current Node를 제거한다.
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            current.next = None
            self.count -= 1
            return current
            





    #-----------------------------------------------------------------------------------
    def insertFront(self, newNode):
        if self.head == None:   # 비어 있는 리스트이므로, 첫 노드 추가 상황이 된다.
            self.head = newNode # self.head => newNode
            self.count = 1      # 
        else:   # 적어도 1개 이상의 노드가 리스트에 연결되어 있는 상황이므로
            newNode.next = self.head # 기존의 첫 노드를 새 노드와 연결한다.  newNode -> head Node
            self.head = newNode # head -> newNode
            self.count += 1

    #-----------------------------------------------------------------------------------
    def append(self, newNode):  # 새 노드(newNode)를 리스트의 마지막에 연결한다.
        if self.head is None:
            self.head = newNode
            self.count = 1
        else:   # 마지막 노드를 찾아서 그 노드의 next에 newNode를 연결한다.
            current = self.head
            while current.next is not None: # current의 다음 노드가 연결되어 있으면 따라간다.
                current = current.next
            # current가 마지막 노드이면 while 종료.
            current.next = newNode
            self.count += 1

    #-----------------------------------------------------------------------------------
    def showList(self):
        print("[Head]->", end="")
        현재노드 = self.head

        while 현재노드 != None:
            print("{}->".format(현재노드), end="")
            현재노드 = 현재노드.next    #다음 연결된 노드로 이동.
        
        print("[Total {} Nodes]".format(self.count))

    #-----------------------------------------------------------------------------------
    def length(self):   # 현재 리스트의 노드 수를 반환한다. (self.count 속성 사용 금지)
        count = 0   # 노드수 계산용 변수
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        
        return count
    #-----------------------------------------------------------------------------------
    def find(self, value):
        current = self.head # 리스트의 head가 가리키는 노드부터 비교 시작.
        while current is not None:
            if value == current.data:
                return current
            else:
                current = current.next
        return None







#==============================================
sl = SList()

sl.append(Node(100))
sl.append(Node(200))
sl.append(Node(300))
sl.showList()
sl.remove(300)
sl.showList()

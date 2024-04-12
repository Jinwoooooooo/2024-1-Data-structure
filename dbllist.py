class Node:
    def __init__(self, data):
        self.data = data    #노드 생성하면서 넘겨준 값을 data 속성에 저장
        self.next = None 

    def __str__(self):
        return f"[{self.data}]"
    
    #---------------------------------------------
class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    #---------------------------------------------
    def __str__(self):
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.data)
            current = current.next
        return str(lst)
    #---------------------------------------------
    #이중 연결 리스트의 맨 앞에 새 노드를 추가하면서 저장할 값을 전달한다.
    def insertFront(self, value):
        #새 노드를 생성하고 , 생성된 노드에 value를 저장한다.
        newNode = Node(value)
        #새 노드가 추가되는 상황을 구분한다. (빈 리스트에 처음 추가하는 경우와, 기존 리스트에 추가하는 경우)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else: #리스트에 노드가 1개 이상 있는 경우
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.count += 1
    #---------------------------------------------
    def append(self, value):
        #새 노드를 생성하고 , 생성된 노드에 value를 저장한다.
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.count += 1
    #---------------------------------------------
    #리스트의 현재 연결 상태를 출력한다.
    def showList(self):
        print("[Head]=", end="")
        현재노드 = self.head
        
        while 현재노드 != None:
            print("{}=".format(현재노드), end="")
            현재노드 = 현재노드.next

        print("[Total {} Nodes]".format(self.count))
    #---------------------------------------------

dlist = DList()
dlist.insertFront(100)
dlist.insertFront(200)
dlist.insertFront(300)
dlist.insertFront(400)
dlist.append(500)
dlist.append(600)
dlist.showList()
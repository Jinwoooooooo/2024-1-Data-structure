class Node:
    def __init__(self, data):
        self.data = data    #노드 생성하면서 넘겨준 값을 data 속성에 저장
        self.prev = None
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
    # 리스트에서 targetNode 앞에 새 노드(value)를 추가한다.
    def insertBefore(self, targetNode, value):
        # targetNode가 None인 경우는 그냥 리턴한다.
        if targetNode is None:
            return
        # Case 1. targetNode가 리스트의 head인 경우 (맨 앞의 노드인 경우)
        if targetNode is self.head:
            self.insertFront(value) # self.count += 1은 insertFront()에 이미 포함됨.
        else:
            # 먼저 새 노드를 생성
            newNode = Node(value)
            # 리스트 완성하기
            newNode.next = targetNode
            newNode.prev = targetNode.prev
            targetNode.prev.next = newNode
            targetNode.prev = newNode
            self.count += 1
    #---------------------------------------------
    # 리스트의 targetNode 뒤에 새 노드(value)를 연결한다.
    def insertAfter(self, targetNode, value):
        # targetNode가 None인 경우는 그냥 리턴한다.
        if targetNode is None:
            return
        
        if targetNode is self.tail:
            self.append(value)
        else:
            # 먼저 새 노드를 생성
            newNode = Node(value)
            # 리스트 완성하기
            newNode.next = targetNode.next
            newNode.prev = targetNode
            targetNode.next.prev = newNode
            targetNode.next = newNode
            self.count += 1
    #---------------------------------------------
    # 오름 차순 정렬 상태를 유지하는 새 노드 (value)의 위치를 찾아서 추가한다.
    # 현재의 리스트는 노드들이 정렬되어 있는 것으로 가정한다. (빈 리스트도 포함)
    def insertSorted(self, value):
        # 1. 빈 리스트인 경우 처리
        if self.count == 0:
            self.append(value)
            return
        # 2. 노드가 하나 이상 있는 경우
        #value보다 크거나 같은 값을 가진 노드를 찾아서 그 노드 앞에 새 노드(value)를 추가한다.
        current = self.head
        while current is not None:
            if current.data >= value:
                self.insertBefore(current, value)
                return
            current = current.next
        # 3. value보다 크거나 같은 노드가 없는 경우에는 리스트의 맨 뒤에 새 노드를 추가한다.
        self.append(value)
        

    #---------------------------------------------
    # 리스트에서 지정된 targetNode를 제거한다.
    # del targetNode (노드 최종 삭제) -> 마지막 단계에서 실행.
    def remove(self, targetNode):
        current = self.head # 연결 리스트의 시작인 head 노드를 current에 할당

        # 첫 번째 노드가 targetNode인 경우
        if current.data == targetNode: # 현재 노드의 데이터가 대상 노드와 일치하는지 확인
            self.head = current.next # 대상 노드가 첫 번째 노드인 경우, 헤드를 대상 노드의 다음 노드로 업데이트
            if self.head: # 새로운 헤드가 존재하는 경우를 확인
                self.head.prev = None # 새로운 헤드의 이전 링크를 None으로 설정하여 연결을 끊음
                self.count -= 1
            return

        # 중간 또는 마지막 노드인 경우
        while current:  # 현재 노드가 존재하는 동안 반복
            if current.data == targetNode: # 현재 노드의 데이터가 대상 노드와 일치하는지 확인
                if current.next: # 현재 노드의 다음 노드가 존재하는지 확인
                    current.next.prev = current.prev # 대상 노드의 다음 노드의 이전 링크를 현재 노드의 이전 링크로 업데이트
                if current.prev: # 현재 노드의 이전 노드가 존재하는지 확인
                    current.prev.next = current.next # 대상 노드의 이전 노드의 다음 링크를 대상 노드의 다음 노드로 업데이트
                    self.count -= 1
                return
            current = current.next

    #---------------------------------------------
    # value 값을 가진 노드를 찾아서 노드를 반환한다. 없으면 None 반환.
    def find(self, value):
        current = self.head # 헤드 노드부터 탐색 시작
        while current is not None:
            if current.data == value:
                return current
            else:
                current = current.next
        return None
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
dlist.append(100)
dlist.append(200)
dlist.append(300)
dlist.append(400)
dlist.append(500)
dlist.append(600)
dlist.showList()

print(dlist.find(200))
# ==== insertBefore ====
n = dlist.find(200)
dlist.insertBefore(n , 150)
dlist.showList()
n = dlist.find(400)
dlist.insertBefore(n , 350)
dlist.showList()

# ==== insertAfter ====
n = dlist.find(500)
dlist.insertAfter(n , 550)
dlist.showList()
n = dlist.find(600)
dlist.insertAfter(n , 650)
dlist.showList()

# ==== insertSorted ====
dlist.insertSorted(250)
dlist.insertSorted(450)
dlist.insertSorted(0)
dlist.insertSorted(50)
dlist.showList()

dlist.remove(0)

dlist.showList()


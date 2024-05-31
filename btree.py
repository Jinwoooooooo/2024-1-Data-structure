import random
from queue2 import *    # BTree의 levelOrder() 등에서 활용하기 위해 가져옴.

#============================================
# class BTree (Binary Tree: 이진트리)
#============================================
class BTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
    #------------------------------------
    def __str__(self):
        r = "[" + str(self.key) + "]"
        return r
    #------------------------------------
    def node(self):      # [None]<-[100]->[None], [50]<-[100]->[None]
        r = ""
        if self.left:
            r += str(self.left)
        else:
            r += "[None]"
        r += "<-" + str(self) + "->"
        if self.right:
            r += str(self.right)
        else:
            r += "[None]"
        return r
    #------------------------------------
    # 전위 순회 (preOrder)
    def preOrder(self):
        print(self, " ", end="")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
    #------------------------------------
    def inOrder(self):  # 왼쪽 서브트리 출력 후, 자신 출력, 오른쪽 서브트리 출력
        if self.left:
            self.left.preOrder()
        print(self, " ", end="")
        if self.right:
            self.right.preOrder()
    #------------------------------------
    def postOrder(self):    # 왼쪽 서브트리 출력, 오른쪽 서브트리 출력, 마지막에 자신 출력
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
        print(self, " ", end="")
    #------------------------------------
    # 트리의 레벨 순서대로 출력, 같은 레벨에서는 왼쪽에서 오른쪽 순서로 출력
    def levelOrder(self):
        queue = Queue()  # 레벨 순서대로 저장할 queue 생성.
        queue.add(self)  # 루트노드 자신을 queue 먼저 저장하고 다음 반복문을 시작

        # queue empty가 될 때까지 반복한다.
        while not queue.isEmpty():
            node = queue.remove()
            print(node, end="")  # 현재 노드를 먼저 출력한다.

            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)

        print("")

    #------------------------------------
    # BTree의 노드 개수를 반환하기
    def nodeCount(self):
        count = 1   # 자신 노드의 개수 먼저 계산.
        if self.left:   #왼쪽 서브트리가 있으면
            count += self.left.nodeCount()  # 왼쪽 서브트리의 노드 개수를 합산
        if self.right:
            count += self.right.nodeCount()

        return count

    #------------------------------------
    # 트리의 높이(height)를 계산하여 반환 (재귀함수 활용)
    def height(self):
        if self.left == None and self.right == None: # 자식 노드가 없으면
            return 1
        elif self.left == None:
            return 1 + self.right.height()
        elif self.right == None:
            return 1 + self.left.height()
        else:
            return max(self.left.height(), self.right.height()) + 1
    #------------------------------------
    # 완전 이진 트리 여부를 확인하여 True, False로 반환한다.
    def isComplete(self):
        queue = Queue()  # 레벨 순서대로 저장할 queue 생성.
        queue.add(self)  # root node부터 queue에 저장.
        danger = False   # 불완전 트리 가능성 발견하면 True로 설정, 이후의 조사에서 참조.

        # queue에서 다음 방문할 노드를 차례대로 꺼내서 조사한다.
        while not queue.isEmpty():       # 방문할 노드가 남아 있으면
            currentNode = queue.remove() # 다음 조사할 노드를 꺼낸다.
            # 왼쪽 자식 노드 상항 처리.
            if currentNode.left:    # 왼쪽 자식 노드가 있고,
                if danger:          # 이전에 위험한 상황(무자식 상황)이 있었으면
                    return False    # 불완전 트리로 결론.
                queue.add(currentNode.left) # 다음에 방문하기 위해 queue에 저장.
            else:
                danger = True

            # 오른쪽 자식 노드 상황 처리
            if currentNode.right:
                if danger:
                    return False
                queue.add(currentNode.right)
            else:
                danger = True

        # while문 종료
        return True # 더 방문할 노드 없이 while 종료되면 완전이진트리 결론.
 
    #------------------------------------
    # 완전 이진 트리를 배열(list)로 변환하기 (list를 반환, 단, 리스트의 첫 항목은 None)
    # 완전 이진 트리가 아닌 경우에는 적절한 오류 메세지 출력과 함께 None를 반환.
    def toList(self):

        if self.isComplete():
            # list로 변환하는 코드 작성.
            lst = [None]
            queue = Queue()  # level Order 방문을 위한 queue 생성.
            queue.add(self)  

            while not queue.isEmpty():
                currentNode = queue.remove()
                lst.append(currentNode.key)
                if currentNode.left:
                    queue.add(currentNode.left)
                if currentNode.right:
                    queue.add(currentNode.right)
            # 최종 리스트 반환
            return lst
        else:
            print("toList: Not Complete Binary Tree.")
            return None


    #------------------------------------
#============================================
# 이진 힙(Binary Heap) 구현하기
#--------------------------------------------
# 최소 힙(Minimum Heap): 값이 작을수록 우선순위가 높다.
class BHeap:
    #----------------------------------------
    # 힙을 구성할 배열(list)를 초기값으로 받는다.
    def __init__(self, a):
        self.a = a  # 힙용 배열(list)
        self.N = len(a) - 1 # 배열의 첫 칸(index=0)은 사용하지 않기 때문에.

    def __str__(self):
        return str(self.a)

    # index i 노드의 자기 위치를 찾아 내려가도록 하는 연산.
    def downHeap(self, i):
        while 2*i <= self.N:
            k = 2*i
            if k < self.N and self.a[k] > self.a[k+1]:  # 오른쪽 자식이 왼쪽 자식보다 우선순위가 높으므로
                k += 1 # 부모 i와 비교할 자식으로 오른쪽 자식으로 수정.
            if self.a[i] < self.a[k]:   # 자식 둘 중의 승자와 부모와의 비교에서 부모의 우선순위가 높다.
                break   # 하강 중단.
            # 부모보다 우선순위가 높은 자식이 결정되었으므로, 자리를 서로 바꾼다.
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k   # downHeap 계속 진행

    def createHeap(self):
        for i in range(self.N//2, -1):
            self.downHeap(i)

#============================================
randMax = 50
random.seed(2024)
root = BTree(random.randint(1, randMax))

queue = Queue()
queue.add(root)
nodeCount = 1

while not queue.isEmpty():
    node = queue.remove()
    leftChild = BTree(random.randint(1, randMax))
    rightChild = BTree(random.randint(1, randMax))
    node.left = leftChild
    node.right = rightChild
    queue.add(leftChild)
    queue.add(rightChild)
    nodeCount += 2

    if nodeCount > 7:
        break
#---------------------------------
# queue 남은 노드들에 대해서만 자식 노드들을 연결한다.
while not queue.isEmpty():
    node = queue.remove()
    leftChild = BTree(random.randint(1, randMax))
    rightChild = BTree(random.randint(1, randMax))
    node.left = leftChild
    node.right = rightChild

#print("Height: {}, Nodes: {}".format(root.height(), root.nodeCount()))
#print("is Complete? {}".format(root.isComplete()))
#lst = root.toList()
#print("List Length: %d\n"%(len(lst)))

lst = root.toList() # 힙용 배열 생성 (완전 이진 트리를 변환., 노드의 값이 우선순위.)
heap = BHeap(lst)
print(heap)
heap.createHeap()
print(heap)






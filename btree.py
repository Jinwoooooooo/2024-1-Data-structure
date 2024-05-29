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
tA = BTree("A")
tB = BTree("B")
tC = BTree("C")
tD = BTree("D")
tE = BTree("E")
tF = BTree("F")
tG = BTree("G")
tH = BTree("H")
tI = BTree("I")
tJ = BTree("J")
#---------------------
tA.left = tB
tA.right = tC
tB.left = tD
tB.right = tE
tD.left = tI
tD.right = tG
tE.left = tH
tC.right = tF
tC.left = tJ
print(tA.toList())


#---------------------
"""
tA.left = tB
tA.right = tC
tB.left = tD
tB.right = tE
tD.right = tG
tE.left = tH
tC.right = tF
#----------------------
treeList = tA.toList()

print("Tree A의 높이는 %d입니다."%(tA.height()))
print("Tree B의 높이는 %d입니다."%(tB.height()))
"""







"""
tA.levelOrder()

print("전위 순회(%9s):"%("preOrder"), end="")
tA.preOrder()
print("")

print("중위 순회(%9s):"%("inOrder"), end="")
tA.inOrder()
print("")

print("후위 순회(%9s):"%("postOrder"), end="")
tA.postOrder()
print("")
"""








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
        pass
    #------------------------------------
    # 완전 이진 트리를 배열(list)로 변환하기 (list를 반환, 단, 리스트의 첫 항목은 None)
    def toList(self):
        pass


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
#---------------------
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








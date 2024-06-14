from btree import *
import random

#========================================
# 이진 탐색 트리 (Binary Search Tree)
#========================================

class BSTree(BTree):
    # 이진 탐색 트리에 새 값을 추가한다.
    # (새 값은 이진 탐색 조건에 맞는 위치에 노드로 추가되어야 한다.)
    def insert(self, value):
        if value < self.key:    # 현재 노드의 왼쪽 어딘가에 추가해야 한다.
            if self.left:       # 왼쪽 자식 서브트리가 있으면
                return self.left.insert(value) # 왼쪽 자식 노드에게 값 추가 처리를 넘긴다. (재귀호출)
            else:               # 왼쪽 자식 서브트리가 없으면
                self.left = BSTree(value)      #현재 노드의 왼쪽 자식(서브트리)으로 새로 등록한다.
                return self.left# 추가된 노드를 처리 결과값으로 반환.
        elif value > self.key:  # 
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTree(value)
                return self.right
        else:   # 현재노드와 같은 값을 추가하는 상황 (새노드로 추가하지 않는다.)
            print("[{}] <== 이미 존재하는 값!!".format(value))
            return None # 새로 추가되지 않았으므로 None, 현재 노드를 반환하는 것도 가능.
        

#====================================================
# 이진 탐색 트리에서 특정 값을 가진 노드를 찾아 반환한다.
# 찾는 값을 가진 노드가 없으면 None을 반환한다.
    def find(self, value):
        if self.key == value:
            return self
        if self.key < value:
            if self.left:   # 왼쪽 서브트리가 있으면
                return self.left.find(value)
            else:
                return None
        else:   # value > self.key
            if self.right:  # 오른쪽 서브트리가 있으면
                return self.right.find(value)   # 오른쪽 서브트리에게 탐색을 맡긴다.
            else:
                return None
#====================================================
# 이진 탐색 트리에 최소값 노드 가져오기
    def minValue(self):
        current = self
        while current.left:
            current = current.left
        return current.key
#====================================================
# 자식 노드가 없으면 True, 아니면 False.
    def hasNoChild(self):
        return self.left == None and self.right == None
#====================================================
# 이진 탐색 트리에 최소값 노드 가져오기
    def minNode(self):
        current = self
        while current.left:
            current = current.left
        return current
#====================================================
# 트리에서 최소값 노드를 삭제한다
# !!! deleteMin()을 호출한 노드의 값을 리턴값으로 업데이트 해야 한다.
    def deleteMin(self):
        if self.left == None:   # self보다 작은 서브트리가 없으므로, self가 삭제 대상이 된다.
            return self.right   # 부모 노드에게 오른쪽 자식으로 연결하도록 반환한다.
        self.left = self.left.deleteMin()
        return self
#====================================================
# 트리에서 특정 값을 가진 노드를 삭제한다. (삭제 후에도 이진 탐색 트리 구조를 유지하는 것이 핵심)
# 반환 값은 삭제 후의 이진 탐색 트리(트리의 루트 노드)를 반환
    def deleteValue(self, value):
        if value < self.key:
            if self.left:
                self.left = self.left.deleteValue(value)
            return self # 본인이(self) 삭제되지 않고 건재함을 알린다. (찾는 값이 없다.)
        elif value > self.key:
            if self.right:
                self.right = self.right.deleteValue(value)
            return self
        else:   # 본인(self)이 삭제 대상. (후계자(부모노드가 가리킬)를 보고한다.)
            if self.hasNoChild():
                return None
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left
            # 본인이 삭제 대상이면서 왼쪽과 오른쪽 서브트리가 모두 존재하는 상황
            # 후계 구도를 정리하고 최종 결과를 부모 노드에게 보고(반환)한다.
            target = self
            successor = self.right.minNode()    # 오른쪽 서브트리에서 가장 작은 노드를 찾는다.
            successor.right = self.right.deleteMin()
            successor.left = target.left
            return successor
#====================================================
# 1 ~ 101 범위의 정수 난수 80개를 생성하여 BSTree에 추가한다.
# 중복된 값을 생성한 경우(insert() 가 None를 리턴한 경우)는 생성 개수에서 제외한다.
bst = BSTree(50)

import random
count = 0
random.seed(20240614)

# 노드 80개 생성하는 코드
count = 0   # 중복 없이 추가된 노드 개수
while count < 80:
    # random number 생성
    rn = random.randint(1, 101)

    # 생성된 random 추가하기
    result = bst.insert(rn)

    # 반환값에 따른 처리
    if result:  # None이 아니면(random number 'rn'이 정상적으로 제자리에 추가되었으면)
        count += 1


# Test
print("노드 개수: {}".format(bst.nodeCount()))
bst.inOrder()
print("\n--------------------------------------------------------------------")
bst = bst.deleteValue(50)
bst.inOrder()
print("\n--------------------------------------------------------------------")
print(bst)




                



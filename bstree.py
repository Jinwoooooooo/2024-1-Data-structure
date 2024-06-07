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
# 1 ~ 101 범위의 정수 난수 80개를 생성하여 BSTree에 추가한다.
# 중복된 값을 생성한 경우(insert() 가 None를 리턴한 경우)는 생성 개수에서 제외한다.
bst = BSTree(50)
    

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




                



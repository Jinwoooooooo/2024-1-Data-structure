from collections import deque

class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = self.right = None
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def preorder(self):
        def _preorder(node):
            print(node.item, end=' ')
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
    
    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.item, end=' ')
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
    
    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.item, end=' ')
        _postorder(self.root)
        
    def levelorder(self):
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.item, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    #BTree의 노드 개수를 반환하기
    def nodeCount(self):
        count = 1   #자신 노드의 개수 먼저 계산.
        if self.left:   #왼쪽 서브트리가 있으면
            count += self.left.nodeCount()  #왼쪽 서브트리의 노드 개수를 합산
        if self.right:  #오른쪽 서브트리가 있으면
            count += self.right.nodeCount() #오른쪽 서브트리의 노드 개수를 합산
        
        return count()
    
    #트리의 높이를 계산하여 반환    
    def height(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return 1 + self.right.height()
        elif self.right == None:
            return 1 + self.left.height()
        else:
            return max(self.left.height(), self.right.height()) + 1

BT = BinaryTree()
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N7 = Node(7)
N8 = Node(8)

BT.root = N1
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7
N4.left = N8

print('preorder')
BT.preorder()

print('\ninorder')
BT.inorder()

print('\npostorder')
BT.postorder()

print('\nlevelorder')
BT.levelorder()
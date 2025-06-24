
#树
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    @classmethod
    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    @classmethod
    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    @classmethod
    def postorder(self, root):
        """递归实现后续遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    @classmethod
    def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print
            node.elem,
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)





# 树


# node

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(ADT):
    def __init__(self):
        pass

class BinTree(Tree):
    def __init__(self):
        # 示例使用
        # 构建二叉树
        #       2
        #      / \
        #     1   4
        #    / \  / \
        #   3  2 5  0
        #  /
        #  9
        self.root = BSTNode(2)

    def CreateBiTree(self):
        self.root.left = BSTNode(1)
        self.root.right = BSTNode(4)
        self.root.left.left = BSTNode(3)
        self.root.left.right = BSTNode(2)
        self.root.right.left = BSTNode(5)
        self.root.right.right = BSTNode(0)
        self.root.left.left.left = BSTNode(9)

    @staticmethod
    def PreOrderTraverse(T,visit=None):
        # TODO 考虑线索化
        if T:
            visit(T.data)
            BinTree.PreOrderTraverse(T.left,visit)
            BinTree.PreOrderTraverse(T.right,visit)

    @staticmethod
    def InOrderTraverse(T,visit=None):
        # TODO 考虑线索化
        if T:
            BinTree.PreOrderTraverse(T.left,visit)
            visit(T.data)
            BinTree.PreOrderTraverse(T.right,visit)


    @staticmethod
    def PostOrderTraverse(T,visit=None):
        # TODO 考虑线索化
        if T:
            BinTree.PreOrderTraverse(T.left,visit)
            BinTree.PreOrderTraverse(T.right,visit)
            visit(T.data)

    @staticmethod
    def LevelOrderTraverse(T,visit):
        # TODO 考虑线索化
        pass


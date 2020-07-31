
# define the node of the tree
class BiTreeNode:
    def __init__(self, val):
        self.val = val
        self.left =None
        self.right = None


# 3种遍历方法

def preorderTrav(subtree: BiTreeNode):
    ''' 先序(根)遍历'''
    if subtree is not None:
        print(subtree.val)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)

def inorderTrav(subtree: BiTreeNode):
    '''中(根)序遍历'''
    if subtree is not None:
        inorderTrav(subtree.left)
        print(subtree.val)
        inorderTrav(subtree.right)

def postorderTrav(subtree: BiTreeNode):
    '''后(根)序遍历'''
    if subtree is not None:
        inorderTrav(subtree.left)
        inorderTrav(subtree.right)
        print(subtree.val)

# BFS bradth-First serach,宽度优先遍历
# 一层一层遍历，使用queue
def bradthFirstTrav(bintree):
    from queue import Queue
    q = Queue()
    q.put(bintree)
    while not q.empty():
        node = q.get()
        print(node.val)
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)

# 表达式树的节点类
class _ExpTreeNode:
    __slots__ = ('element', 'left', 'right')

    def __init__(self,data):
        self.element = data
        self.left = None
        self.right = None

    def __repr__(self):
        # 将实例转换为字符串时定义
        # 注意与__str__区分
        return '<_ExpTreeNode:{} {} {}>'.format(self.element, self.left,self.right)

from queue import Queue
class ExpressionTree:
    '''
        表达式树: 操作符存储在内节点操作数存储在叶子节点的二叉树。(符号树真难打出来)
        *
       / \
      +   -
     / \  / \
     9  3 8   4
    (9+3) * (8-4)

    Expression Tree Abstract Data Type，可以实现二元操作符
    ExpressionTree(expStr): user string as constructor param
    evaluate(varDict): evaluates the expression and returns the numeric result
    toString(): constructs and retutns a string represention of the expression

    Usage:
        vars = {'a': 5, 'b': 12}
        expTree = ExpressionTree("(a/(b-3))")
        print('The result = ', expTree.evaluate(vars))
    '''

    def __init__(self, expStr):
        self._expTree = None
        self._buildTree(expStr)



     
    def evaluate(self, varDict):
        pass


root = BiTreeNode(5)
left_tRoot = BiTreeNode(3)
right_tRoot = BiTreeNode(7)
root.left = left_tRoot
root.right = right_tRoot
left_tRoot.left = BiTreeNode(2)
left_tRoot.right = BiTreeNode(4)
right_tRoot.left = BiTreeNode(6)
right_tRoot.right = BiTreeNode(8)

bradthFirstTrav(root)

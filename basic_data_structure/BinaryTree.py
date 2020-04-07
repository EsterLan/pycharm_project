
# define the node of the tree
class BiTreeNode:
    def __init__(self, val):
        self._val = val
        self._left =None
        self._right = None


# 3种遍历方法

def preoderTrav(root: BiTreeNode):
    if root is None:
        return
    else:
    
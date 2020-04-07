# 单链表
class ListNode():
    def __init__(self, data, nextNode = None):
        self.data = data
        self.next = nextNode


# def travsersal(head: ListNode, callback):
#     """
#     遍历链表
#     :param head:
#     :param callback:?
#     :return:
#     """
#     pass

def unorderedSearch(head:ListNode, target)-> bool:
# def unorderedSearch(self, target) -> bool:

    """
    无序查找 target是否在LinkedList中
    :param head:
    :param target:
    :return:
    """
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None


def append(self, item):
    """
    在链表尾端添加item
    :param item:
    :return:
    """
    newNode = ListNode(item)
    curNode = self._head
    while curNode.next is not None:
        curNode = curNode.next
    curNode.next = newNode

def prepend(head: ListNode, item):
    "    向前添加. Given the head pointer, prepend an item to an usnsorted linked list"
    newNode = ListNode(item, head)
    head = newNode
    # 需要对节点返回，这是因为这仅仅式函数 而不是方法， 此处head与形参无关，仅仅是一个变量，不返回 无法对实参有任何影响
    return head

def remove(head:ListNode, target):
    """
    Given the head reference, remove the target from a linkedList
    :param head:
    :return:
    """
    predNode = None # the Node before curNode
    curNode = head
    while curNode is not None and curNode.data != target:
        # 遍历寻找target
        predNode = curNode
        curNode = curNode.next
    # curNode非空表示寻找到了目标
    if curNode is not None:
        # 若本身只有一个节点且为目标的情况
        if curNode == head:
            head.next = curNode.next
        else:
            # remove the curNode
            predNode.next = curNode.next


def printNode(head: ListNode):
    while head is not None:
        print(head.data)
        head = head.next


l = ListNode(1)
prepend(l,2) #
printNode(l)
print("------")
remove(l, 1)
l.next = ListNode(3)
printNode(l)

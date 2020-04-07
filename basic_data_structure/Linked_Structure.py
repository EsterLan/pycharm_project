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

class LinkedList():
    def __init__(self, head: ListNode):
        self._head = head

    # def unorderedSearch(head:ListNode, target)-> bool:
    def unorderedSearch(self, target) -> bool:

        """
        无序查找 target是否在LinkedList中
        :param head:
        :param target:
        :return:
        """
        curNode = self._head
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
    # def prepend(head: ListNode, item):
    def prepend(self, item):

        """
        向前添加. Given the head pointer, prepend an item to an usnsorted linked list
        :param head: ListNode, the head pointer to be prepended
        :param item:
        :return: ListNode
        """
        newNode = ListNode(item, self._head)
        self._head = newNode
        # newNode = Node(item, head)
        # self.head = newNode

        # temp = ListNode(item)
        # temp.next = head.next
        # head.next = temp


    def remove(self, target):
        """
        Given the head reference, remove the target from a linkedList
        :param head:
        :return:
        """
        predNode = None # the Node before curNode
        curNode =self._head
        while curNode is not None and curNode.data != target:
            # 遍历寻找target
            predNode = curNode
            curNode = curNode.next
        # curNode非空表示寻找到了目标
        if curNode is not None:
            # 若本身只有一个节点且为目标的情况
            if curNode == self._head:
                self._head.next = curNode.next
            else:
                # remove the curNode
                predNode.next = curNode.next

    def printNode(self):
        curNode = self._head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next


l = LinkedList(ListNode(1))
l.append(3)
l.prepend(2)
l.prepend(4)
l.printNode()
print(l.unorderedSearch(2))
l.remove(3)
l.printNode()
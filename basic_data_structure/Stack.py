# class Stack(object):
#     'Using a Python list.FILO'
#     def __init__(self):
#         self._items = list()
#
#     def isEmpty(self):
#         return len(self) == 0
#
#     def __len__(self):
#         return len(self._items)
#
#     def pop(self):
#         # 判断是否为空
#         assert not self.isEmpty()
#         return self._items.pop()
#
#     def push(self, item):
#         self._items.append(item)
#
#     def peek(self):
#         # 仅返回值，对栈不做更改
#         assert not self.isEmpty()
#         return self._items[-1]
class Stack:
    """
     Stack ADT, use linked list
    使用list实现很简单，但是如果涉及大量push操作，list的空间不够时复杂度退化到O(n)
    而linked list可以保证最坏情况下仍是O(1)
    """
    def __init__(self):
        self._top = None # top节点， StackNode or None
        self._size = 0 # int

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def pop(self):
        assert not self.isEmpty()
        curNode = self._top
        v = curNode.item
        self._top = curNode.next
        self._size -= 1
        return v

    def push(self, item):
        # self._top.next = self._top
        # self._top.item =item
        self._top = StackNode(item, self._top)
        self._size += 1

    def peek(self):
        assert not self.isEmpty()
        return self._top.item


class StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

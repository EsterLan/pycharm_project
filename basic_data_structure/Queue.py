# class Queue:
#     """Queue ADT, using a Python list.
#     list实现，简单但是push和pop效率最差是O(n)
#     Queue()
#     isEmpty()
#     length()
#     enqueue(item)
#     dequeue()
#     """
#     def __init__(self):
#         self._items = list()
#
#     def isEmpty(self):
#         return len(self._items) == 0
#
#     def __len__(self):
#         return len(self._items)
#
#     def enqueue(self, item):
#         self._items.append(item)
#
#     def dequeue(self):
#         assert not self.isEmpty()
#         item = self._items[0]
#         self._items.pop(0)
#         return item

# class Queue:
#     """ Queue ADT, linked list 实现。为了改进环型数组有最大数量的限制，改用
#     带有头尾节点的linked list实现。
#     """
#     def __init__(self):
#         self._qhead = None
#         self._qtail = None
#         self._qsize = 0
#
#     def isEmpty(self):
#         return self._qhead is None
#
#     def __len__(self):
#         return self._count
#
#     def enqueue(self, item):
#         node = QueueNode(item)    # 创建新的节点并用尾节点指向他
#         if self.isEmpty():
#             self._qhead = node
#         else:
#             self._qtail.next = node
#         self._qtail = node
#         self._qcount += 1
#
#     def dequeue(self):
#         assert not self.isEmpty(), 'Can not dequeue from an empty queue'
#         node = self._qhead
#         if self._qhead is self._qtail:
#             self._qtail = None
#         self._qhead = self._qhead.next    # 前移头节点
#         self._count -= 1
#         return node.item

class Queue:
    """ Queue ADT, using a linked list

    """
    def __init__(self):
        self._qhead = None # 头节点， QueueNode or None
        self._qtail = None # 尾节点
        self._size = 0

    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._size

    def enqueue(self, item):
        newNode = QueueNode(item)
        if self.isEmpty():
            self._qhead = newNode
            self._qhead.next = self._qtail
            self._qtail = newNode
        else:
            self._qtail.next = newNode
            self._qtail = self._qtail.next
        self._size += 1

    def dequeue(self):
        assert not self.isEmpty() # can't dequeue from a empty queue
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._size -= 1
        return node.item


class UboundedPriorityQueue:
    """
     PriorityQueue ADT: 给每个item加上优先级p，高优先级先dequeue
    分为两种：
    - bounded PriorityQueue: 限制优先级在一个区间[0...p)
    - unbounded PriorityQueue: 不限制优先级
    PriorityQueue()
    BPriorityQueue(numLevels): create a bounded PriorityQueue with priority in range
        [0, numLevels-1]
    isEmpty()
    length()
    enqueue(item, priority): 如果是bounded PriorityQueue, priority必须在区间内
    dequeue(): 最高优先级的出队，同优先级的按照FIFO顺序
       - 两种实现方式：
    1.入队的时候都是到队尾，出队操作找到最高优先级的出队，出队操作O(n)
    2.始终维持队列有序，每次入队都找到该插入的位置，出队操作是O(1)
    (注意如果用list实现list.append和pop操作复杂度会因内存分配退化)
    """
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    # def unorderedSort(self):
    #     if not( self.isEmpty() or self._size ==1):
    #

    def enqueue(self, item, p):
        newNode = PQueueNode(item, p)
        if self.isEmpty():
            self._qhead = newNode
            self._qhead.next = self._qtail
            self._qtail = newNode
        else:
            self._qtail.next = newNode
            self._qtail = self._qtail.next

        self._size += 1

    def dequeue(self):
        assert not self.isEmpty()
        prepMax = None  # 出栈要对出栈元素的前一元素进行存储
        maxP = self._qhead
        if self._qhead is self._qtail:
            prepMax = self._qhead
            self._qtail = None
        else:
            node = self._qhead
            while node.next is not None:
                if node.next.p > maxP.p:
                    prepMax = node
                    maxP = node.next
                else:
                    prepMax = self._qhead
                node = node.next
        prepMax.next = maxP.next
        self._size -= 1
        return maxP.item


class PQueueNode:
    def __init__(self, item, p):
        self.item = item
        self.next = None
        self.p = p  # priority


class QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None


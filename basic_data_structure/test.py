import basicSorting
import advancedSorting
# import Solution

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2, end = m-1, n-1, m+n-1
        while l1>=0 and l2>=0:
            if nums1[l1] > nums2[l2]:
                nums1[end] = nums1[l1]
                l1 -= 1
            else:
                nums1[end] = nums2[l2]
                l2 -= 1
            end -= 1
        if l1 < 0: # nums2 left
            nums1[:l2] = nums2[:l2]

l = [1,2,3,4,5]
# print(basicSorting.binarySearch(l, 10))
l1 = [4,3,2,5,1]
l2 = [1, 5, 3, 9,1]
l3 = [4,7,9,10]
# print(basicSorting.selection_sort(l1))
# print(basicSorting.insertion_sort(l1))
# print(basicSorting.merge_sorted_list(l,l3))
# print(advancedSorting.mergeSort(l3))
# print(advancedSorting.quick_sort(l2, 0, len(l2)-1))
# l1 = [1,3,4,0, 0, 0]
# l2 = [2,5,6]
# sol = Solution()
# sol.merge(l1, 3, l2, 3)
# print(l1)
print(advancedSorting.nth_element(l2,0,len(l2)-1,2))



from Queue import Queue, UboundedPriorityQueue

q = Queue()
q.enqueue(1)
q.enqueue([1,2,3])
q.enqueue("stella")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

pq = UboundedPriorityQueue()
pq.enqueue(1,1.4)
pq.enqueue("he",1.2)
pq.enqueue("she", 12)
pq.enqueue("stella maxwell",1)
item = pq.dequeue()
print(item)


from Stack import Stack
s = Stack()
s.push(1)
s.push("hehe")
s.push("hi")
s.push(4)
print(s.peek())
print(s.pop())
print(s.peek())


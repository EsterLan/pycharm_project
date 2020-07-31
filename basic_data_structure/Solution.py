class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 二分查找
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[-1]
        lo = 0
        hi = len(rotateArray) -1
        while lo <= hi:
            mid = (lo+hi)//2
            if rotateArray[mid] < rotateArray[lo]:
                # mid处于第二个有序数列中
                hi = mid
            elif rotateArray[mid] > rotateArray[lo]:
                lo = mid + 1
            else:
                #lo += 1
                hi -= 1
        return rotateArray[lo]

# class Solution1:
#     def Fibonacci(self, n):
#         # write code here
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.Fibonacci(n-1) + self.Fibonacci(n-2)


# -*- coding:utf-8 -*-
class Solution2:
    def reOrderArray(self, array):
        # write code here
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        # lo = 0
        hi = len(array) - 1
        lo = mid
        while lo>=0:
            if array[lo] % 2 == 1:
                # 前半部分，遇到奇数后移一位
                lo -= 1
            elif array[hi] % 2 == 0:
                # 后半部分， 遇到偶数向前移一位
                hi -= 1
            else:
                # 若有一不满足，则交换位置
                array[lo], array[hi] = array[hi], array[lo]


class Solution3:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
            # 长度不等
            return False

        temp = []
        popV = popV[::-1]
        for i in range(len(pushV)):
            temp.append(pushV[i])
            while temp[-1] == popV[-1] and len(temp) != 0 and len(popV) != 0:
                # 若压入元素为弹出序列的首个元素，则将该元素弹出，并且popV的第一个元素也弹出
                temp.pop()
                popV.pop()
        return len(popV) == 0


# -*- coding:utf-8 -*-
class Solution4:
    def verifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        elif len(sequence) == 1 or len(sequence) == 2:
            # 序列长度为1或者2，必为BST的后续遍历结果
            return True
        elif len(sequence) == 3:
            # 考虑lambda表达式代替
            if sequence[0] < sequence[-1] and sequence[1] > sequence[-1]:
                return False
            else:
                return True
        else:
            root = sequence.pop()
            i = -1
            right_tree = []
            while i >= len(sequence) * (-1) and sequence[i] > root:
                right_tree.append(sequence.pop())
                i -= 1
            left_tree = sequence
            return self.verifySquenceOfBST(right_tree) and self.verifySquenceOfBST(left_tree)

class Solution5:
    def NumberOf1Between1AndN(self, n)->int:
        if n < 2**63-1:
            l = list(range(1, n+1))
            power = len(str(n))
            res = sum([i%10==1 for i in l])
            for p in range(1, power):
                res += sum([i//(10**p)==1 for i in l])
            return res

class Solution6:
    def PrintMinNumber(self, numbers):
        length = len(numbers)
        str_num = [str(i) for i in numbers]
        min_num = int(''.join(str_num))
        for j in range(length):
            a = str_num[j]
            new_str = [i for i in str_num if i != str_num[j]]
            cur = a + new_str
            cur = int(cur)
            if cur < min_num:
                min_num = cur
        return min_num

s = Solution()
a = s.minNumberInRotateArray([6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335])
print(a)
# s1 = Solution1()
# b = s1.Fibonacci(3)
s2 = Solution2()
c = [1,2,3,4,5,6,7]
s2.reOrderArray(c)
s3 = Solution3()
# s3.IsPopOrder([1,2,3,4,5],[4,5,3,2,1])
s4 = Solution4()
print(s4.verifySquenceOfBST([4,3,6,5,50,100,7]))

s5 =Solution5()
print(s5.NumberOf1Between1AndN(10000))

s6 = Solution6()
print(s6.PrintMinNumber([3,5,1,2,4]))

#print(c)
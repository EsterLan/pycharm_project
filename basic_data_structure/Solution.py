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

class Solution1:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

s = Solution()
a = s.minNumberInRotateArray([6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335])
print(a)
s1 = Solution1()
b = s1.Fibonacci(3)
print(b)
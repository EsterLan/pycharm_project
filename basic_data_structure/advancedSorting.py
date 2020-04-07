from basicSorting import merge_sorted_list

def mergeSort(l: list)-> list:
    """From Up to Bottom, recursively implement
        先递归再排序
    """
    # 基线条件
    if len(l) <= 1:
        return l
    else:
        mid = len(l)//2
        # 为何此处不能为mid+1
        # 首先len(l)>=2, 不需要考虑前半部分无元素（且:0也取得出元素
        # 其次考虑 len(l) = 2时， 会进入四循环，递归无法返回的情况。
        lefthalf = mergeSort(l[:mid])
        righthalf = mergeSort(l[mid:])
    # 合并两有序数组
        return merge_sorted_list(lefthalf, righthalf)


def merge(l: list, lo:int, mid: int, hi: int)-> list:
    '对一个数组实行原地归并'
    i = lo
    j = mid+1
    lux = [0 for i in range(len(l))]
    for k in range(len(l)):
        if i > mid:
            lux[k] = l[j]
            j += 1
        elif j > hi:
            lux[k] = l[i]
            i+=1
        elif l[j] <l[i]:
            lux[k] = l[j]
            j += 1
        else:
            lux[k] = l[i]
            i += 1
    return lux

def mergeSortBU(l: list)->list:
    'BOTTOM UP'
    # while sz <
    pass


def quick_sort(l: list, lo: int, hi: int) -> list:
    """
        选定pivot， 分别对list中小于pivot和大于pivot的值进行排序
        先排序再递归
    """
    # 基线条件
    if hi <= lo:
        return l
    else:
        j = partition(l, lo, hi)
        left_to_j = quick_sort(l, lo, j-1)
        right_to_j = quick_sort(l, j+1, hi)
        return l


def partition(l:list, lo: int, hi: int) -> int:
    """
    对l[lo:hi]进行切分，使代切分元素左侧元素均小于pivot，其右侧元素均大于pivot
    :param l: 待处理list
           lo: 起始元素的indx
           hi: 末尾元素的indx
    :return: 切分元素在列表l中的位置
    """
    i = lo
    j = hi
    while True:
        v = l[lo]  # 切分元素为传入的首个元素
        while l[i] <= v and i < hi:
            # 从左往右搜索， <=pivot的元素跳过，指针右移直至到hi
            # 有>pivot的元素跳出循环
            i += 1
        while l[j] >= v and j > lo:
            # 从hi开始往左搜索， >= pivot的元素跳过，指针左移直到lo
            # 有<pivot的元素，跳出循环
            j -= 1
        if i >= j:
            # 指针相遇时 break出整个循环
            break
        # 将pivot两侧的元素交换
        exch(l, i, j)
    # pivot与j处元素交换
    exch(l, lo, j)
    # 返回切分元素的索引
    return j


def nth_element(l:list, beg:int, end: int, k:int):
    if beg == end:
        return l[beg]
    pivot_index = partition(l, beg, end)
    if k< pivot_index+1:
        return nth_element(l, beg, pivot_index-1,k)
    elif k > pivot_index+1:
        return nth_element(l, pivot_index+1, end, k-pivot_index)
    else:
        return l[pivot_index]



def exch(l: list, i: int, j: int):
    l[i], l[j] = l[j], l[i]




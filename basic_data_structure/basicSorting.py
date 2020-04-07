def binarySearch(sorted_seq: list, target)->int:
    '二分查找'
    low = 0
    high = len(sorted_seq) - 1
    assert (target in sorted_seq)
    while low <= high:
        cur = (high + low)//2
        if target < sorted_seq[cur]:
            # 目标位于左半部分
            high = cur
            continue
        elif target > sorted_seq[cur]:
            # 目标位于右半部分
            low = cur
        else:
            return cur


def bubble_sort(seq: list)-> list:
    pass


def selection_sort(seq: list)->list:
    assert (len(seq)!= 0)
    for cur_begin in range(0,len(seq)):
        min = cur_begin
        # 从cur_begin开始向后搜索最小元素
        for i in range(cur_begin, len(seq)):
            if seq[i] < seq[min]:
                min = i
        exch(seq, min, cur_begin)
    return seq


def insertion_sort(seq: list)->list:
    assert (len(seq) != 0)
    for cur in range(0, len(seq)):
        # 找到插入的合适位置,并交换
        # 后续可以对
        for i in range(0, cur):
            if seq[cur] <= seq[i]:
                exch(seq, cur, i)   
    return seq


def merge_sorted_list(seq1: list, seq2: list)->list:
    'seq1,seq2为有序列表时，仅原地归并'
    lo = 0
    hi = len(seq1) + len(seq2)
    mid = len(seq1)-1
    seq = seq1 + seq2
    sequx = [0 for i in range(hi)]
    i = lo
    j = mid+1
    for k in range(len(seq)):
        if i > mid:
            # 左半边元素取完后对右边有序元素复制
            sequx[k] = seq[j]
            j += 1
        elif j > hi:
            # 右边元素取完后对左边元素复制
            sequx[k] = seq[i]
            i += 1
        elif seq[j] < seq[i]:
            # 右边元素小于左边元素取右边元素
            sequx[k] = seq[j]
            j += 1
        else:
            # 左边元素小于等于右边元素取左边元素
            sequx[k] = seq[i]
            i += 1
    return sequx

def exch(seq:list, i, j):
    temp = seq[i]
    seq[i], seq[j] = seq[j], temp
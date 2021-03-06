def qsort1(alist):
    """out-in-place 非原地快排"""
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        return qsort1([x for x in alist[1:] if x < pivot]) + [pivot] + qsort1([x for x in alist[1:] if x >= pivot])


def qsort2(alist, l, r):
    """in-place 原地快排
    l:开始位置
    u:结束位置
    """
    if l >= r:
        return
    m = l
    for i in range(l + 1, r + 1):
        if alist[i] < alist[l]:
            m += 1
            alist[m], alist[i] = alist[i], alist[m]
    # swap between m and l after partition, important!
    alist[m], alist[l] = alist[l], alist[m]
    qsort2(alist, l, m - 1)
    qsort2(alist, m + 1, r)


def qsort3(alist, lower, upper):
    """使用两个索引分别向右向左进行partition"""
    if lower >= upper:
        return
    pivot = alist[lower]
    left, right = lower + 1, upper
    while left <= right:
        while left <= right and alist[left] < pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            break
        # swap while left <= right
        alist[left], alist[right] = alist[right], alist[left]
    # swap the smaller with pivot
    alist[lower], alist[right] = alist[right], alist[lower]

    qsort3(alist, lower, right - 1)
    qsort3(alist, right + 1, upper)


if __name__ == '__main__':
    unsortedArray = input()
    # 6 5 3 1 8 7 2 4
    unsortedArray = list(map(int, unsortedArray.split(' ')))
    # print(qsort1(unsortedArray))
    # qsort2(unsortedArray, 1, len(unsortedArray) - 2)
    qsort2(unsortedArray, 0, len(unsortedArray) - 1)
    # qsort3(unsortedArray, 0, len(unsortedArray) - 1)
    print(unsortedArray)

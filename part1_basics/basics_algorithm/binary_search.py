def binary_search(seq, v, low, high):
    while low <= high:
        mid = int((low + high) / 2)
        if v == seq[mid]:
            return mid
        elif v > seq[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_target(array, target):
    """寻找第一个或者最后一个，该target元素出现的位置的问题"""
    if not array:
        return -1

    start, end = 0, len(array) - 1
    while start + 1 < end:
        mid = int((start + end) / 2)
        if array[mid] == target:
            start = mid
        elif array[mid] < target:
            start = mid
        else:
            end = mid

    if array[start] == target:
        return start
    if array[end] == target:
        return end
    return -1


def search_range(array, target):
    ret = [-1, -1]
    if not array:
        return ret
    # search first position of target
    st, ed = 0, len(array) - 1
    while st + 1 < ed:
        mid = int((st + ed) / 2)
        if array[mid] == target:
            ed = mid
        elif array[mid] < target:
            st = mid
        else:
            ed = mid
    if array[st] == target:
        ret[0] = st
    elif array[ed] == target:
        ret[0] = ed

    # search last position of target
    st, ed = 0, len(array) - 1
    while st + 1 < ed:
        mid = int((st + ed) / 2)
        if array[mid] == target:
            st = mid
        elif array[mid] < target:
            st = mid
        else:
            ed = mid
    if array[ed] == target:
        ret[1] = ed
    elif array[st] == target:
        ret[1] = st

    return ret


if __name__ == '__main__':
    arr = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search_range(arr, 8))

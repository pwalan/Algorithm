import sys


def qsort(alist):
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        return qsort([x for x in alist[1:] if x < pivot]) + [pivot] + qsort([x for x in alist[1:] if x >= pivot])


def search_range(array, target):
    ret = [-1, -1]
    if not array:
        return ret

    st, ed = 0, len(array) - 1
    while st + 1 < ed:
        mid = int((st + ed) / 2)
        if array[mid] == target:
            ed = mid
        elif array[mid] < target:
            st = mid
        else:
            ed = mid
    ret[0] = st
    ret[1] = ed
    return ret


if __name__ == "__main__":
    line0 = sys.stdin.readline().strip().split()
    n = int(line0[0])
    A = []
    line1 = sys.stdin.readline().strip().split()
    for i in range(n):
        A.append(int(line1[i]))

    for i in range(1, n):
        tmpA = A[:i]
        tmpA = qsort(tmpA)
        bs = search_range(tmpA, A[i])
        v1 = abs(A[i] - tmpA[bs[0]])
        v2 = abs(A[i] - tmpA[bs[1]])
        if v1 < v2:
            print(str(v1) + " " + str(tmpA[bs[0]]))
        else:
            print(str(v2) + " " + str(tmpA[bs[1]]))

    # for j in range(i):
    #     res = abs(A[i] - A[j])
    #     if res < minA:
    #         minA = res
    #         minAJ = A[j]
    # print(str(minA) + " " + str(minAJ))

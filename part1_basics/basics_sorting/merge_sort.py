
def merge(L, R):
    tmp = []
    h = j = 0
    while j < len(L) and h < len(R):
        if L[j].upper() <= R[h].upper():
            tmp.append(L[j])
            j += 1
        else:
            tmp.append(R[h])
            h += 1

    if j == len(L):
        for i in R[h:]:
            tmp.append(i)
    else:
        for i in L[j:]:
            tmp.append(i)

    return tmp


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = int(len(lists) / 2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)
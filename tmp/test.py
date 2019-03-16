import sys


class Node():
    def __init__(self, prev, next, score, count):
        self.prev = prev
        self.next = next
        self.score = score
        self.count = count


def count_present(a):
    mina = min(a)
    minNode = Node(None, None, 0, 0)
    nodes = []
    for i in range(len(a)):
        nodes.append(Node(None, None, a[i], 0))
    nodes[0].next = nodes[1]
    nodes[0].prev = nodes[-1]
    nodes[-1].prev = nodes[-2]
    nodes[-1].next = nodes[0]
    if mina == a[0]:
        minNode = nodes[0]
        minNode.count = 1
    if mina == a[-1]:
        minNode = nodes[-1]
        minNode.count = 1

    for i in range(1, len(a) - 1):
        nodes[i].prev = nodes[i - 1]
        nodes[i].next = nodes[i + 1]
        if mina == a[i]:
            minNode = nodes[i]
            minNode.count = 1

    node = minNode.next
    node.score = 2
    res = 3
    while node != minNode:
        if node.next.score > node.score:
            node.next.count = node.count + 1
            res += node.count + 1
        else:
            node.next.count = node.count - 1
            res += node.count - 1
        node = node.next

    print(res)


if __name__ == "__main__":
    line0 = sys.stdin.readline().strip().split()
    N = int(line0[0])
    a = []
    for _ in range(N):
        n = int(sys.stdin.readline().strip())
        tmp = []
        line1 = sys.stdin.readline().strip().split()
        for i in range(n):
            tmp.append(int(line1[i]))
        a.append(tmp)
    for i in range(N):
        count_present(a[i])

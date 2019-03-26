class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left, self.right = left, right


# 根据前序和中序遍历重构树
def construct_tree(pre_order, mid_order):
    if pre_order is None or mid_order is None:
        return None
    if len(pre_order) == 0 or len(mid_order) == 0:
        return None

    root_data = pre_order[0]
    i = mid_order.index(root_data)

    left = construct_tree(pre_order[1: 1 + i], mid_order[:i])
    right = construct_tree(pre_order[1 + i:], mid_order[i + 1:])
    return TreeNode(root_data, left, right)


class Traversal(object):
    def __init__(self):
        self.traverse_path = list()

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)


def serial_by_pre(head: TreeNode):
    if head is None:
        return "#_"
    res = head.val + "_"
    res += serial_by_pre(head.left)
    res += serial_by_pre(head.right)
    return res


if __name__ == "__main__":
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    # pre_order = []
    mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
    # mid_order = []
    tn = construct_tree(pre_order, mid_order)
    ts = Traversal()
    ts.postorder(tn)
    print(ts.traverse_path)

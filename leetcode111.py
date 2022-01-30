class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mindepth(root):
    if root is None:
        return 0
    p = [root]
    current_level_num = 1
    next_level_num = 0
    i = 1
    while p:
        current = p.pop(0)
        current_level_num -= 1
        if current.left is None and current.right is None:
            return i
        if current.left:
            next_level_num += 1
            p.append(current.left)
        if current.right:
            next_level_num += 1
            p.append(current.right)
        if current_level_num == 0:
            i += 1
            current_level_num = next_level_num
            next_level_num = 0
    return current_level_num


right_tree = TreeNode(20)
right_tree.right = TreeNode(7)
right_tree.left = TreeNode(15)

left_tree = TreeNode(9)

tree = TreeNode(3)
tree.left = left_tree
tree.right = right_tree

a=mindepth(tree)
print(a)

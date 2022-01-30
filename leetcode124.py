# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return m(root)[1]


def m(tree):
    """
    single: 只包含一个方向（左右）的最大路径
    total : 包含两个方向（左和右）的最大路径
    """
    if not tree: return 0, 0
    ls, lt = m(tree.left)
    rs, rt = m(tree.right)
    single = tree.val+max(0, ls, rs)
    if ls > 0 and rs > 0:
        total = tree.val + ls + rs
    else:
        total = single
    if tree.left and lt > total: total = lt
    if tree.right and rt > total: total = rt
    return single, total


right_tree = TreeNode(20)
right_tree.right = TreeNode(7)
right_tree.left = TreeNode(15)

left_tree = TreeNode(9)

root = TreeNode(3)
root.right = right_tree
root.left = left_tree
print(Solution().maxPathSum(root))
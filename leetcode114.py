# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        :type root: TreeNode
        :rtype: int
        """
        # 左子树为空，直接考虑下个点
        while root:
            # 记录左子树最右边节点
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 左子树最右边节点连上当前节点右子树
                pre.right = root.right
                root.right = root.left
                root.left = None
                # 下一个
            root = root.right
            return root


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right = TreeNode(5)
tree.right.right = TreeNode(6)

print(Solution().flatten(tree).val)  # 此处输出的是root的右儿子

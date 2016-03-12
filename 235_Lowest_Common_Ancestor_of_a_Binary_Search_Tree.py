# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def nextStep(treeNode):
          if p.val > treeNode.val:
            return nextStep(treeNode.right)
          elif q.val < treeNode.val:
            return nextStep(treeNode.left)
          else:
            return treeNode

        if p.val > q.val:
          temp = p
          p = q
          q = temp

        return nextStep(root)


s = Solution()
# s.lowestCommonAncestor()

#       _______6______
#      /              \
#   ___2__          ___8__
#  /      \        /      \
# 0      _4       7       9
#       /  \
#       3   5
'''
Problem:
Given the root of a binary tree, invert the tree, and return its root.
'''

'''
Logic: To invert a tree, all we need to do is swap the left and right children of each node. We can utilize recursion to do this. We first
check if root pointer is currently on a node, if not we can end the recursive call. Else, we will swap the children and recursively call
the function on the left and right children. We can then return the root pointer.
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional['TreeNode']:
        if not preorder or not postorder:
            return None
        
        # The first element in preorder is the root.
        root = TreeNode(preorder[0])
        
        # If there's only one element, return it.
        if len(preorder) == 1:
            return root
        
        # The second element in preorder is the root of the left subtree.
        left_root_val = preorder[1]
        # Find left_root_val in postorder to determine the size of left subtree.
        L = postorder.index(left_root_val) + 1  # size of left subtree in postorder
        
        # Recursively construct left and right subtrees.
        root.left = self.constructFromPrePost(preorder[1:L+1], postorder[:L])
        root.right = self.constructFromPrePost(preorder[L+1:], postorder[L:-1])
        
        return root

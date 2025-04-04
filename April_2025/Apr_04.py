# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_map = {}
        self.compute_max_depth(root, 0, depth_map)
        overall_max = depth_map.get(root, 0)
        return self.find_lca(root, overall_max, depth_map)
    
    def compute_max_depth(self, node, current_depth, depth_map):
        if not node:
            return 0
        left_max = self.compute_max_depth(node.left, current_depth + 1, depth_map)
        right_max = self.compute_max_depth(node.right, current_depth + 1, depth_map)
        if node.left is None and node.right is None:
            current_max = current_depth
        else:
            current_max = max(left_max, right_max)
        depth_map[node] = current_max
        return current_max
    
    def find_lca(self, node, overall_max, depth_map):
        if not node:
            return None
        left_max = depth_map.get(node.left, 0) if node.left else 0
        right_max = depth_map.get(node.right, 0) if node.right else 0
        if left_max == overall_max and right_max == overall_max:
            return node
        if left_max == overall_max:
            return self.find_lca(node.left, overall_max, depth_map)
        if right_max == overall_max:
            return self.find_lca(node.right, overall_max, depth_map)
        if not node.left and not node.right and depth_map.get(node, 0) == overall_max:
            return node
        return None

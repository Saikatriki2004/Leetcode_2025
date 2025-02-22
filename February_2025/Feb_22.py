# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> 'TreeNode':
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # Count the dashes to determine the depth.
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Parse the number (it can have multiple digits)
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            # Create a new TreeNode with the parsed value.
            node = TreeNode(val)
            
            # If stack size is greater than depth, pop until they are equal.
            while len(stack) > depth:
                stack.pop()
            
            # Attach the node as a child of the last node in the stack.
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Push the current node onto the stack.
            stack.append(node)
        
        # The root is at the bottom of the stack (first element).
        return stack[0]

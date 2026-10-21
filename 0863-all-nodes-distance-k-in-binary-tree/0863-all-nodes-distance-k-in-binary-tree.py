from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Record parent pointers for each node
        parent = {}
        def dfs(node, par=None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        # Step 2: BFS from the target node
        queue = deque([(target, 0)])
        visited = {target}
        res = []
        
        while queue:
            node, dist = queue.popleft()
            
            if dist == k:
                res.append(node.val)
            elif dist < k:
                # Check left child, right child, and parent
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
                        
        return res
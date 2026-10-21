from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start_r, start_c = -1, -1
        total_keys = 0
        
        # Locate start and count keys
        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell == '@':
                    start_r, start_c = r, c
                elif 'a' <= cell <= 'f':
                    total_keys = max(total_keys, ord(cell) - ord('a') + 1)
        
        # Queue stores: (row, col, keys_mask, steps)
        queue = deque([(start_r, start_c, 0, 0)])
        visited = set([(start_r, start_c, 0)])
        
        target_mask = (1 << total_keys) - 1
        
        while queue:
            r, c, keys, steps = queue.popleft()
            
            if keys == target_mask:
                return steps
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    cell = grid[nr][nc]
                    
                    if cell == '#':
                        continue
                    
                    # Check if it's a lock and we don't have the key
                    if 'A' <= cell <= 'F':
                        lock_idx = ord(cell) - ord('A')
                        if not (keys & (1 << lock_idx)):
                            continue
                    
                    next_keys = keys
                    # Check if it's a key
                    if 'a' <= cell <= 'f':
                        key_idx = ord(cell) - ord('a')
                        next_keys |= (1 << key_idx)
                        
                    if (nr, nc, next_keys) not in visited:
                        visited.add((nr, nc, next_keys))
                        queue.append((nr, nc, next_keys, steps + 1))
                        
        return -1
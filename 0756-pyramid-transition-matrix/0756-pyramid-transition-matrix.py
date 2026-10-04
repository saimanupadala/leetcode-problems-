from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Build transition mapping: (left, right) -> list of possible top blocks
        transitions = defaultdict(list)
        for pattern in allowed:
            transitions[(pattern[0], pattern[1])].append(pattern[2])
        
        memo = set()

        def can_build_next_level(current_row: str) -> bool:
            # Base case: top of the pyramid reached
            if len(current_row) == 1:
                return True
            
            # If this row was already proven impossible, skip
            if current_row in memo:
                return False
            
            # Generate next rows recursively
            next_rows = []
            
            def generate_rows(index: int, built_row: list[str]):
                if index == len(current_row) - 1:
                    next_rows.append("".join(built_row))
                    return
                
                pair = (current_row[index], current_row[index + 1])
                for top in transitions.get(pair, []):
                    built_row.append(top)
                    generate_rows(index + 1, built_row)
                    built_row.pop()

            generate_rows(0, [])
            
            # Try each valid next row
            for next_row in next_rows:
                if can_build_next_level(next_row):
                    return True
            
            # Cache row as unsolvable
            memo.add(current_row)
            return False

        return can_build_next_level(bottom)
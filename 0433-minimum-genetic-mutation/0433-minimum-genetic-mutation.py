from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

        # If endGene is not in the bank, mutation is impossible
        if endGene not in bank:
            return -1

        bank = set(bank)

        queue = deque([(startGene, 0)])
        visited = {startGene}

        genes = ['A', 'C', 'G', 'T']

        while queue:
            current, steps = queue.popleft()

            # We reached the target
            if current == endGene:
                return steps

            # Try changing every character
            for i in range(8):
                for gene in genes:

                    if gene == current[i]:
                        continue

                    new_gene = current[:i] + gene + current[i + 1:]

                    # Valid mutation
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))

        return -1
        
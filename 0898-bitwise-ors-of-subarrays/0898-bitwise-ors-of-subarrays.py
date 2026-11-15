
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        curr = set()

        for num in arr:
            new_set = {num}

            for x in curr:
                new_set.add(x | num)

            curr = new_set
            result.update(curr)

        return len(result)

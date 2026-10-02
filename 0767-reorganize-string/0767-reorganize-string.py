class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq

        count = Counter(s)

        # Max heap: (-frequency, character)
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        result = []

        while heap:
            freq1, ch1 = heapq.heappop(heap)

            # If the same character would be adjacent
            if result and result[-1] == ch1:
                if not heap:
                    return ""

                freq2, ch2 = heapq.heappop(heap)

                result.append(ch2)
                freq2 += 1

                if freq2 < 0:
                    heapq.heappush(heap, (freq2, ch2))

                heapq.heappush(heap, (freq1, ch1))
            else:
                result.append(ch1)
                freq1 += 1

                if freq1 < 0:
                    heapq.heappush(heap, (freq1, ch1))

        return "".join(result)
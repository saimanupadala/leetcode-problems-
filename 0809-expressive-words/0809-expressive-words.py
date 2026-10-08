class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(string: str):
            """Compress string into list of (char, count) tuples."""
            groups = []
            for char in string:
                if groups and groups[-1][0] == char:
                    groups[-1][1] += 1
                else:
                    groups.append([char, 1])
            return groups

        s_groups = compress(s)
        stretchy_count = 0

        for word in words:
            w_groups = compress(word)

            # Sequence of distinct characters must match in length
            if len(s_groups) != len(w_groups):
                continue

            is_stretchy = True
            for (s_char, s_len), (w_char, w_len) in zip(s_groups, w_groups):
                # Characters must match
                if s_char != w_char:
                    is_stretchy = False
                    break

                # Word group cannot be larger than s group
                if w_len > s_len:
                    is_stretchy = False
                    break

                # If word group is smaller, s group must be at least 3
                if w_len < s_len and s_len < 3:
                    is_stretchy = False
                    break

            if is_stretchy:
                stretchy_count += 1

        return stretchy_count
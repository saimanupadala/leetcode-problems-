class Solution:
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if typ == "start":
                # Current function runs until this new function starts
                if stack:
                    result[stack[-1]] += time - prev_time

                stack.append(fid)
                prev_time = time

            else:  # end
                # +1 because end timestamp is inclusive
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        
        max_profit = 0
        best_profit = 0
        i = 0
        
        worker.sort()
        
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                best_profit = max(best_profit, jobs[i][1])
                i += 1
            
            max_profit += best_profit
        
        return max_profit

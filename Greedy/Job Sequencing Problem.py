class Solution:
    @staticmethod
    def solve(ids, deadlines, profits):
        jobs = [(ids[i], deadlines[i], profits[i]) for i in range(len(ids))]
        jobs.sort(key=lambda x: x[2], reverse=True)
        days_tracker = {i: None for i in range(1, max(deadlines) + 1)}
        net_profit = 0
        for job in jobs:
            id, deadline, profit = job
            start_index = deadline
            while start_index >= 1:
                if days_tracker[start_index] is None:
                    days_tracker[start_index] = id
                    net_profit += profit
                    break
                else:
                    start_index -= 1
        jobs_performed = {k: v for k, v in days_tracker.items() if v is not None}
        return list(jobs_performed.values()), net_profit


print(Solution.solve([1, 2, 3, 4], [4, 1, 1, 1], [20, 1, 40, 30]))
print(Solution.solve([1, 2, 3, 4, 5], [2, 1, 2, 1, 1], [100, 19, 27, 25, 15]))

class Job:
    def __init__(self, s, e, p):
        self.start_time = s
        self.end_time = e
        self.profit = p


class RecursiveSolution:
    @staticmethod
    def schedule(start_times, end_times, profits):
        """
            Time complexity is exponential and space complexity is O(n).
        """
        jobs = [Job(start_times[i], end_times[i], profits[i]) for i in range(len(start_times))]
        jobs.sort(key=lambda x: x.start_time)
        return RecursiveSolution._get_max_profit(jobs, 0, len(jobs))

    @staticmethod
    def _get_max_profit(jobs, i, n):
        """
            Time complexity is exponential and space complexity is O(n).
        """
        if i >= n:
            return 0
        left = jobs[i].profit + RecursiveSolution._get_max_profit(jobs, RecursiveSolution._get_next_job(jobs, i, n), n)
        right = RecursiveSolution._get_max_profit(jobs, i + 1, n)
        return max(left, right)

    @staticmethod
    def _get_next_job(jobs, i, n):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        low, high = i + 1, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            possible_next_job = jobs[mid]
            if possible_next_job.start_time >= jobs[i].end_time:
                high = mid - 1
            else:
                low = mid + 1
        return low


print("Recursive Approach")
print(
    RecursiveSolution.schedule(
        [1, 3, 6, 2],
        [2, 5, 19, 100],
        [50, 20, 100, 200]
    )
)

print(
    RecursiveSolution.schedule(
        [1, 2, 4, 5],
        [3, 5, 6, 7],
        [60, 50, 70, 30]
    )
)


print(
    RecursiveSolution.schedule(
        [1, 2, 3, 3],
        [3, 4, 5, 6],
        [50, 10, 40, 70]
    )
)

print(
    RecursiveSolution.schedule(
        [1, 2, 3, 4, 6],
        [3, 5, 10, 6, 9],
        [20, 20, 100, 70, 60]
    )
)

print(
    RecursiveSolution.schedule(
        [1, 1, 1],
        [2, 3, 4],
        [5, 6, 4]
    )
)

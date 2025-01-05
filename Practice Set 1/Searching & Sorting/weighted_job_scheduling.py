class Job:
    def __init__(self, start, end, profit):
        self.start_time = start
        self.end_time = end
        self.profit = profit


class RecursiveSolution:
    @staticmethod
    def _get_jobs(jobs, start_times, end_times, profits):
        n = len(start_times)
        for i in range(n):
            jobs.append(
                Job(
                    start_times[i],
                    end_times[i],
                    profits[i]
                )
            )

    @staticmethod
    def _get_next_job_index(jobs, low, high, end_time):
        while low <= high:
            mid = int(low + (high - low)/2)
            job = jobs[mid]
            if job.start_time == end_time:
                high = mid - 1
            elif job.start_time < end_time:
                low = mid + 1
            else:
                high = mid - 1
        return low

    @staticmethod
    def _solve(jobs, index, n):
        if index >= n:
            return 0
        next_job_index = RecursiveSolution._get_next_job_index(jobs, index + 1, n - 1, jobs[index].end_time)
        take = jobs[index].profit + RecursiveSolution._solve(jobs, next_job_index, n)
        not_take = RecursiveSolution._solve(jobs, index + 1, n)
        return max(take, not_take)

    @staticmethod
    def schedule(start_times, end_times, profits):
        """
            Overall time complexity is exponential and space complexity is O(n).
        """
        jobs = []
        RecursiveSolution._get_jobs(jobs, start_times, end_times, profits)
        # This will take O(n * log(n)) to sort.
        jobs.sort(key=lambda x: x.start_time)
        # This method is exponential in time and O(n) in space.
        return RecursiveSolution._solve(jobs, 0, len(jobs))


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
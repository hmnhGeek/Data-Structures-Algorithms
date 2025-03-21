# Problem link - https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/
# Solution - https://www.youtube.com/watch?v=LL0tVxlAeV4&t=14s


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


class MemoizedSolution:
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
    def _solve(jobs, index, n, dp):
        if index >= n:
            return 0
        if dp[index] is not None:
            return dp[index]
        next_job_index = MemoizedSolution._get_next_job_index(jobs, index + 1, n - 1, jobs[index].end_time)
        take = jobs[index].profit + MemoizedSolution._solve(jobs, next_job_index, n, dp)
        not_take = MemoizedSolution._solve(jobs, index + 1, n, dp)
        dp[index] = max(take, not_take)
        return dp[index]

    @staticmethod
    def schedule(start_times, end_times, profits):
        """
            Overall time complexity is O(n * log(n)) and space complexity is O(n).
        """
        jobs = []
        MemoizedSolution._get_jobs(jobs, start_times, end_times, profits)
        # This will take O(n * log(n)) to sort.
        jobs.sort(key=lambda x: x.start_time)
        dp = {i: None for i in range(len(jobs))}
        # This method is O(n) in time and O(n) in space.
        return MemoizedSolution._solve(jobs, 0, len(jobs), dp)


class TabulationSolution:
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
    def schedule(start_times, end_times, profits):
        """
            Overall time complexity is O(n * log(n)) and space complexity is O(n).
        """
        jobs = []
        TabulationSolution._get_jobs(jobs, start_times, end_times, profits)
        n = len(jobs)

        # This will take O(n * log(n)) to sort.
        jobs.sort(key=lambda x: x.start_time)

        dp = {i: 0 for i in range(n + 1)}
        for index in range(n - 1, -1, -1):
            next_job_index = TabulationSolution._get_next_job_index(jobs, index + 1, n - 1, jobs[index].end_time)
            take = jobs[index].profit + dp[next_job_index]
            not_take = dp[index + 1]
            dp[index] = max(take, not_take)
        # This method is O(n) in time and O(n) in space.
        return dp[0]


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

print("Memoized Approach")
print(
    MemoizedSolution.schedule(
        [1, 3, 6, 2],
        [2, 5, 19, 100],
        [50, 20, 100, 200]
    )
)

print(
    MemoizedSolution.schedule(
        [1, 2, 4, 5],
        [3, 5, 6, 7],
        [60, 50, 70, 30]
    )
)

print("Tabulation Approach")
print(
    TabulationSolution.schedule(
        [1, 3, 6, 2],
        [2, 5, 19, 100],
        [50, 20, 100, 200]
    )
)

print(
    TabulationSolution.schedule(
        [1, 2, 4, 5],
        [3, 5, 6, 7],
        [60, 50, 70, 30]
    )
)

print(
    TabulationSolution.schedule(
        [1, 2, 3, 3],
        [3, 4, 5, 6],
        [50, 10, 40, 70]
    )
)

print(
    TabulationSolution.schedule(
        [1, 2, 3, 4, 6],
        [3, 5, 10, 6, 9],
        [20, 20, 100, 70, 60]
    )
)

print(
    TabulationSolution.schedule(
        [1, 1, 1],
        [2, 3, 4],
        [5, 6, 4]
    )
)
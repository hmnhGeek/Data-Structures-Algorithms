# Problem link - https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/
# Solution - https://www.youtube.com/watch?v=LL0tVxlAeV4&t=14s


from typing import List


class Job:
    def __init__(self, start_time, end_time, profit):
        self.start_time = start_time
        self.end_time = end_time
        self.profit = profit


class RecursiveSolution:
    """
        Time complexity is exponential and space complexity is O(n).
    """
    @staticmethod
    def _find_next_possible_job_index(jobs: List[Job], index: int, n: int) -> int:
        end_time_of_current_job = jobs[index].end_time
        low, high = index + 1, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if jobs[mid].start_time >= end_time_of_current_job:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def _find_max_profit(jobs: List[Job], index: int, n: int) -> int:
        if index >= n:
            return 0
        next_possible_job_index = RecursiveSolution._find_next_possible_job_index(jobs, index, n)
        left = jobs[index].profit + RecursiveSolution._find_max_profit(jobs, next_possible_job_index, n)
        right = RecursiveSolution._find_max_profit(jobs, index + 1, n)
        return max(left, right)

    @staticmethod
    def schedule(jobs: List[Job]) -> int:
        jobs.sort(key=lambda x: x.start_time)
        n = len(jobs)
        return RecursiveSolution._find_max_profit(jobs, 0, n)


class MemoizedSolution:
    """
        Time complexity is O(n + n*log(n)) and space complexity is O(2n).
    """
    @staticmethod
    def _find_next_possible_job_index(jobs: List[Job], index: int, n: int) -> int:
        end_time_of_current_job = jobs[index].end_time
        low, high = index + 1, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if jobs[mid].start_time >= end_time_of_current_job:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def _find_max_profit(jobs: List[Job], index: int, n: int, dp) -> int:
        if index >= n:
            return 0
        if dp[index] is not None:
            return dp[index]
        next_possible_job_index = MemoizedSolution._find_next_possible_job_index(jobs, index, n)
        left = jobs[index].profit + MemoizedSolution._find_max_profit(jobs, next_possible_job_index, n, dp)
        right = MemoizedSolution._find_max_profit(jobs, index + 1, n, dp)
        dp[index] = max(left, right)
        return dp[index]

    @staticmethod
    def schedule(jobs: List[Job]) -> int:
        jobs.sort(key=lambda x: x.start_time)
        n = len(jobs)
        dp = {i: None for i in range(n)}
        return MemoizedSolution._find_max_profit(jobs, 0, n, dp)


class TabulationSolution:
    """
        Time complexity is O(n * log(n)) and space complexity is O(n).
    """
    @staticmethod
    def _find_next_possible_job_index(jobs: List[Job], index: int, n: int) -> int:
        end_time_of_current_job = jobs[index].end_time
        low, high = index + 1, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if jobs[mid].start_time >= end_time_of_current_job:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def schedule(jobs: List[Job]) -> int:
        jobs.sort(key=lambda x: x.start_time)
        n = len(jobs)
        dp = {i: 0 for i in range(n + 2)}
        for index in range(n - 1, -1, -1):
            next_possible_job_index = TabulationSolution._find_next_possible_job_index(jobs, index, n)
            left = jobs[index].profit + dp[next_possible_job_index]
            right = dp[index + 1]
            dp[index] = max(left, right)
        return dp[0]


print("Recursive Solution")
print(
    RecursiveSolution.schedule(
        [
            Job(1, 2, 50),
            Job(3, 5, 20),
            Job(6, 19, 100),
            Job(2, 100, 200)
        ]
    )
)

print(
    RecursiveSolution.schedule(
        [
            Job(1, 3, 60),
            Job(2, 5, 50),
            Job(4, 6, 70),
            Job(5, 7, 30)
        ]
    )
)

print(
    RecursiveSolution.schedule(
        [
            Job(1, 3, 50),
            Job(2, 4, 10),
            Job(3, 5, 40),
            Job(3, 6, 70)
        ]
    )
)

print(
    RecursiveSolution.schedule(
        [
            Job(1, 3, 20),
            Job(2, 5, 20),
            Job(3, 10, 100),
            Job(4, 6, 70),
            Job(6, 9, 60)
        ]
    )
)

print(
    RecursiveSolution.schedule(
        [
            Job(1, 2, 5),
            Job(1, 3, 6),
            Job(1, 4, 4)
        ]
    )
)

print()
print("Memoized Solution")
print(
    MemoizedSolution.schedule(
        [
            Job(1, 2, 50),
            Job(3, 5, 20),
            Job(6, 19, 100),
            Job(2, 100, 200)
        ]
    )
)

print(
    MemoizedSolution.schedule(
        [
            Job(1, 3, 60),
            Job(2, 5, 50),
            Job(4, 6, 70),
            Job(5, 7, 30)
        ]
    )
)

print(
    MemoizedSolution.schedule(
        [
            Job(1, 3, 50),
            Job(2, 4, 10),
            Job(3, 5, 40),
            Job(3, 6, 70)
        ]
    )
)

print(
    MemoizedSolution.schedule(
        [
            Job(1, 3, 20),
            Job(2, 5, 20),
            Job(3, 10, 100),
            Job(4, 6, 70),
            Job(6, 9, 60)
        ]
    )
)

print(
    MemoizedSolution.schedule(
        [
            Job(1, 2, 5),
            Job(1, 3, 6),
            Job(1, 4, 4)
        ]
    )
)


print()
print("Tabulation Solution")
print(
    TabulationSolution.schedule(
        [
            Job(1, 2, 50),
            Job(3, 5, 20),
            Job(6, 19, 100),
            Job(2, 100, 200)
        ]
    )
)

print(
    TabulationSolution.schedule(
        [
            Job(1, 3, 60),
            Job(2, 5, 50),
            Job(4, 6, 70),
            Job(5, 7, 30)
        ]
    )
)

print(
    TabulationSolution.schedule(
        [
            Job(1, 3, 50),
            Job(2, 4, 10),
            Job(3, 5, 40),
            Job(3, 6, 70)
        ]
    )
)

print(
    TabulationSolution.schedule(
        [
            Job(1, 3, 20),
            Job(2, 5, 20),
            Job(3, 10, 100),
            Job(4, 6, 70),
            Job(6, 9, 60)
        ]
    )
)

print(
    TabulationSolution.schedule(
        [
            Job(1, 2, 5),
            Job(1, 3, 6),
            Job(1, 4, 4)
        ]
    )
)

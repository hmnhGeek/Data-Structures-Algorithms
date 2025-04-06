from typing import List


class Job:
    def __init__(self, start_time, end_time, profit):
        self.start_time = start_time
        self.end_time = end_time
        self.profit = profit


class RecursiveSolution:
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

# print(
#     RecursiveSolution.schedule(
#         [1, 2, 4, 5],
#         [3, 5, 6, 7],
#         [60, 50, 70, 30]
#     )
# )
#
#
# print(
#     RecursiveSolution.schedule(
#         [1, 2, 3, 3],
#         [3, 4, 5, 6],
#         [50, 10, 40, 70]
#     )
# )
#
# print(
#     RecursiveSolution.schedule(
#         [1, 2, 3, 4, 6],
#         [3, 5, 10, 6, 9],
#         [20, 20, 100, 70, 60]
#     )
# )
#
# print(
#     RecursiveSolution.schedule(
#         [1, 1, 1],
#         [2, 3, 4],
#         [5, 6, 4]
#     )
# )
# Problem link - https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
# Solution - https://www.youtube.com/watch?v=LL0tVxlAeV4

class Job:
    def __init__(self, start_time, end_time, profit):
        self.start = start_time
        self.end = end_time
        self.profit = profit


def get_next_available_job(jobs, low, end_time):
    # since the jobs are sorted on start times, we can perform a binary search
    # to find that start time which >= end time.

    # low = index + 1, high = n - 1
    high = len(jobs) - 1

    # typical binary search algorithm.
    while low <= high:
        mid = int(low + (high - low)/2)

        # if the current job's start time is >= end time, let's search in the left part.
        # maybe there could be a job with lower start time >= end time.
        if jobs[mid].start >= end_time:
            high = mid - 1
        else:
            # if the start time of mid-job is less than end time, let's move higher up
            # to increase the start time.
            low = mid + 1

    # at the end, low will be at that index where first start time value such that
    # start time >= end time is found. return it.
    return low


def solve(jobs, index):
    # This will take O(log(n) * 2^n) time and O(n) space.

    # base case: if the current index is out of bounds, no profit can be made.
    if index >= len(jobs):
        return 0

    # if you've considered this job, start searching from the next index for a job
    # whose start time is >= end_time of this job. This will take O(log(n)) time.
    next_available_job_index = get_next_available_job(jobs, index + 1, jobs[index].end)

    # return the maximum profit obtained by not considering this job and by considering this job.
    # When not considering, simply move to next index without adding profit of current job, and
    # in considering case add current job's profit and move to the next available job index instead
    # of the immediate next job.
    return max(solve(jobs, index + 1), jobs[index].profit + solve(jobs, next_available_job_index))


def get_max_profit(jobs):
    # Overall time complexity is O(n * log(n) + log(n) * 2^n) and space complexity is O(n).

    # sort the jobs based on start time, this will take O(n * log(n))
    jobs.sort(key=lambda x: x.start)

    # return the max profit by starting from the 0th job.
    return solve(jobs, 0)

print(
    get_max_profit(
        [
            Job(3, 5, 20),
            Job(2, 100, 200),
            Job(1, 2, 50),
            Job(6, 19, 100)
        ]
    )
)

print(
    get_max_profit(
        [
            Job(1, 3, 50),
            Job(3, 5, 40),
            Job(2, 4, 10),
            Job(3, 6, 70)
        ]
    )
)

print(
    get_max_profit(
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
    get_max_profit(
        [
            Job(1, 2, 5),
            Job(1, 3, 6),
            Job(1, 4, 4)
        ]
    )
)
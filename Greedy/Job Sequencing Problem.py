class Solution:
    @staticmethod
    def solve(ids, deadlines, profits):
        """
            Overall time complexity is O(nlog(n) + n*m) and space complexity is O(n).
        """

        # construct a matrix by combining the above three lists. This will take O(3 * n) space.
        jobs = [(ids[i], deadlines[i], profits[i]) for i in range(len(ids))]

        # sort the jobs based on profits in descending order in O(n * log(n)) time.
        jobs.sort(key=lambda x: x[2], reverse=True)

        # create a days tracking hash map with O(max(deadlines)) = O(m) space.
        days_tracker = {i: None for i in range(1, max(deadlines) + 1)}

        # define a net profit variable.
        net_profit = 0

        # loop on the jobs in n iterations
        for job in jobs:
            id, deadline, profit = job

            # traceback from deadline index till the first day.
            start_index = deadline
            while start_index >= 1:
                # if the current day is available, do this job. Basically, we are trying to do a job at the very end,
                # but within its timeline.
                if days_tracker[start_index] is None:
                    days_tracker[start_index] = id
                    net_profit += profit
                    break
                else:
                    start_index -= 1

        # get the jobs which are actually done.
        jobs_performed = {k: v for k, v in days_tracker.items() if v is not None}

        # return the job ids which are performed and the net profit.
        return list(jobs_performed.values()), net_profit


print(Solution.solve([1, 2, 3, 4], [4, 1, 1, 1], [20, 1, 40, 30]))
print(Solution.solve([1, 2, 3, 4, 5], [2, 1, 2, 1, 1], [100, 19, 27, 25, 15]))
print(Solution.solve([1, 2, 3, 4], [3, 1, 2, 2], [50, 10, 20, 30]))
print(Solution.solve([1, 2, 3], [1, 1, 1], [40, 50, 60]))

# Problem link - https://www.geeksforgeeks.org/the-celebrity-problem/#expected-approach-using-two-pointers-on-time-and-o1-space
# Solution - https://www.youtube.com/watch?v=cEadsbTeze4


class Solution:
    @staticmethod
    def find_celebrity(mtx):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(mtx)
        top, down = 0, n - 1

        # while top is less than down
        while top < down:
            # if top knows down, then top can't be a celebrity.
            if mtx[top][down] == 1:
                top += 1
            # else if down knows top, down cannot be a celebrity.
            elif mtx[down][top] == 1:
                down -= 1
            # if both don't know each other, they both can't be a celebrity, because a celebrity must be known by every
            # one else. They are just simple individuals.
            else:
                top += 1
                down -= 1

        # at end, if pointers come down to a single person...
        if top == down:
            # if this single person knows even one other person, they are not a celebrity.
            for i in range(n):
                if top != i and mtx[top][i] == 1:
                    return -1

            # if even a single other person does not know this person, this person is not a celebrity.
            for i in range(n):
                if top != i and mtx[i][top] == 0:
                    return -1

            # if everything goes fine, then this person is a celebrity, return it.
            return top
        return -1


print(Solution.find_celebrity([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]))
print(Solution.find_celebrity([[0, 1], [1, 0]]))
print(Solution.find_celebrity([[0]]))
print(Solution.find_celebrity([[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]))

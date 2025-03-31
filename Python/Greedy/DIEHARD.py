# Problem link - https://www.spoj.com/problems/DIEHARD/
# Solution - https://www.youtube.com/watch?v=KrXzcYTDn2s


def get_next(i):
    d = {
        1: [3, 2],
        2: [-5, -10],
        3: [-20, 5]
    }
    return {k: v for k, v in d.items() if k != i}


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(i, j, e):
        # at any point if the health or the armor becomes <= 0, return 0
        if i <= 0 or j <= 0:
            return 0

        # get the other 2 elements other than `e`.
        d = get_next(e)

        # recursively get the max time to live.
        result = 0
        for k, v in d.items():
            result = max(result, 1 + solve(i + v[0], j + v[1], k))
        return result

    def diehard(health, armor):
        result = 0
        # search for the maximum by starting on all the 3 elements.
        for i in range(1, 4):
            result = max(result, solve(health, armor, i))
        return result - 1

    print(diehard(20, 20))
    print(diehard(20, 8))
    print(diehard(4, 4))
    print(diehard(2, 10))


def memoized():
    """
        Time complexity is O(3*h*a) and space complexity is O(h + a + h * a * 3).
    """

    def solve(i, j, e, dp):
        # at any point if the health or the armor becomes <= 0, return 0
        if i <= 0 or j <= 0:
            return 0

        if dp[i][j][e] is not None:
            return dp[i][j][e]

        # get the other 2 elements other than `e`.
        d = get_next(e)

        # recursively get the max time to live.
        result = 0
        for k, v in d.items():
            result = max(result, 1 + solve(i + v[0], j + v[1], k, dp))
        dp[i][j][e] = result
        return dp[i][j][e]

    def diehard(health, armor):
        result = 0
        dp = {i: {j: {e: None for e in range(1, 4)} for j in range(-20, 100)} for i in range(-20, 100)}
        # search for the maximum by starting on all the 3 elements.
        for i in range(1, 4):
            result = max(result, solve(health, armor, i, dp))
        return result - 1

    print(diehard(20, 20))
    print(diehard(20, 8))
    print(diehard(4, 4))
    print(diehard(2, 10))


recursive()
print()
memoized()
print()

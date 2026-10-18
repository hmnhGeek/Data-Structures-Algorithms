class Solution:
    @staticmethod
    def get_longest_string_chain(strings):
        n = len(strings)
        strings.sort(key = len)
        dp = {i: 1 for i in range(n)}
        parent = {i: i for i in range(n)}
        for i in range(n):
            for prev in range(i):
                if unit_diff(strings[i], strings[prev]) and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    parent[i] = prev
        start_index = max(dp, key=dp.get)
        result = []
        while start_index != parent[start_index]:
            result.append(strings[start_index])
            start_index = parent[start_index]
        result.append(strings[start_index])
        return result[-1:-len(result)-1:-1]


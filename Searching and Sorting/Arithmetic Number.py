class Solution:
    @staticmethod
    def is_ap_no(a, b, c):
        res = (b - a)/c + 1
        return int(res) == res


print(Solution.is_ap_no(1, 3, 2))
print(Solution.is_ap_no(1, 2, 3))
print(Solution.is_ap_no(1, 2, 4))
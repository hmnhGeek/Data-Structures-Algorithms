def to_the_power(a, n):
    # returns a^n in O(log(n)) time
    ans = 1

    while n > 0:
        if n % 2 == 1:
            ans *= a
            n -= 1
        else:
            a *= a
            n /= 2

    return ans


print(to_the_power(2, 5))
print(to_the_power(31, 2))
print(to_the_power(-1, 4))
print(to_the_power(-7, 3))
print(to_the_power(0, 100))
print(to_the_power(1032, 0))
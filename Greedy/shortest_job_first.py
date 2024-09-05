def sjf(jobs):
    jobs.sort()
    n = len(jobs)
    wait_time = 0
    t = 0
    for i in range(n):
        wait_time += t
        t += jobs[i]
    return int(wait_time / n)


print(sjf([4, 3, 7, 1, 2]))

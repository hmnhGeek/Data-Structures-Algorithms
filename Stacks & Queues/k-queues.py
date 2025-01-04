from math import ceil


class KQueues:
    def __init__(self, n, k):
        self.arr = [None] * n
        self.num_queues = ceil(n / k)
        self.starts = [i for i in range(0, n, k)]
        self.ends = [i + min(k, n - i) for i in range(0, n, k)]
        self.tops = [i for i in range(0, n, k)]
        self.k = k

    def push(self, x, q):
        if q > self.num_queues or q <= 0:
            return
        queue_index = q - 1
        top = self.tops[queue_index]
        if top in range(self.starts[queue_index], self.ends[queue_index]):
            self.arr[top] = x
            self.tops[queue_index] += 1
        else:
            print("Overflow!")

    def pop(self, q):
        queue_index = q - 1
        top = self.tops[queue_index]
        if top == queue_index * self.k:
            return None
        top -= 1
        item = self.arr[top]
        self.arr[top] = None
        return item


kq = KQueues(10, 3)
kq.push(1, 4)
kq.push(3, 4)
kq.push(10, 2)
kq.push(11, 2)
kq.push(12, 2)
kq.push(13, 2)
kq.push(13, 3)
print(kq.pop(4))
print(kq.pop(4))
print(kq.arr)

# Problem link - https://www.geeksforgeeks.org/efficiently-implement-k-queues-single-array/


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
        # if the queue asked for does not exist
        if q > self.num_queues or q <= 0:
            return

        # get the index of the queue and then the top pointer of it.
        queue_index = q - 1
        top = self.tops[queue_index]

        # if top pointer is still in the range of k, add the element
        if top in range(self.starts[queue_index], self.ends[queue_index]):
            self.arr[top] = x
            self.tops[queue_index] += 1
        else:
            # else print overflow.
            print("Overflow!")

    def pop(self, q):
        # if the queue asked for does not exist
        if q > self.num_queues or q <= 0:
            return

        # get the actual index of the queue and the top pointer.
        queue_index = q - 1
        top = self.tops[queue_index]

        # since top points to a null location and if top is at the beginning of the queue, there's nothing to pop.
        if top == queue_index * self.k:
            return None

        # else go to the next non-None index and return it.
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

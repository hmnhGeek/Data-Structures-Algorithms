# Problem link - https://www.geeksforgeeks.org/dsa/efficiently-implement-k-stacks-single-array/
# Solution - https://www.youtube.com/watch?v=lrSXKLmnMV8


class KStacks:
    def __init__(self, n, k):
        self.arr = [None] * n
        self.tops = [-1] * k
        self.next = [i + 1 for i in range(n)]
        self.next[-1] = -1
        self.free_spot = 0

    def push(self, x, m):
        # get the free spot index
        index = self.free_spot

        # update the free spot
        self.free_spot = self.next[index]

        # add the element into the stack
        self.arr[index] = x

        # update the next array
        self.next[index] = self.tops[m]

        # update the top
        self.tops[m] = index
        print(1)

    def pop(self, m):
        if self.tops[m] == -1:
            return None

        # get the top of the stack and retrieve the item from the stack
        index = self.tops[m]
        item = self.arr[index]

        # make the arr at this index null.
        self.arr[index] = None

        # update the top to the next index.
        self.tops[m] = self.next[index]

        # update the next to free spot
        self.next[index] = self.free_spot

        # update the free spot to the index value.
        self.free_spot = index

        # return the item
        return item


stacks = KStacks(5, 4)
stacks.push(15, 0)
stacks.push(25, 1)
stacks.push(35, 2)
stacks.push(45, 3)
stacks.push(55, 0)
print(stacks.pop(0))
print(stacks.pop(1))
stacks.push(55, 0)
print(stacks.pop(3))

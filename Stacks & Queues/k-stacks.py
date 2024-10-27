import math


class kStacks:
    def __init__(self, array_capacity, k):
        self.stack_array = [None]*array_capacity
        self.k = k
        self.n = array_capacity
        self.num_stacks = math.ceil(array_capacity/k)
        self.pointers = [i - 1 for i in range(0, array_capacity, k)]
        print(f"Initialized {self.num_stacks} stacks each of {self.k} slots.")

    def push(self, stack_no, elem):
        print(f"Pushing {elem} on stack {stack_no}.")
        low = self.k * (stack_no - 1)
        high = self.k * stack_no if stack_no * self.k < self.n else self.n
        top = self.pointers[stack_no - 1]
        if low - 1 <= top < high - 1:
            self.stack_array[top + 1] = elem
            self.pointers[stack_no - 1] += 1
        else:
            print(f"Overflow on stack number {stack_no}")
        print(self.pointers, self.stack_array)

    def pop(self, stack_no):
        print(f"Popping from stack {stack_no}.")
        low = self.k * (stack_no - 1)
        high = self.k * stack_no if stack_no * self.k < self.n else self.n - 1
        top = self.pointers[stack_no - 1]
        if top == low - 1:
            print(f"Stack number {stack_no} is empty!")
            print(self.pointers, self.stack_array)
            return
        item = self.stack_array[top]
        self.stack_array[top] = None
        self.pointers[stack_no - 1] -= 1
        print(self.pointers, self.stack_array)
        return item


stacks = kStacks(10, 3)

stacks.push(2, 11)

stacks.push(2, 100)

stacks.push(2, 150)

stacks.push(2, 16)

stacks.push(3, 101)

stacks.push(3, 1111)

stacks.push(3, -11)

stacks.push(3, 99)

stacks.push(4, 101)

stacks.push(4, 56)

stacks.pop(1)

stacks.push(1, -1)
# Problem link - https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/


import math


class kStacks:
    def __init__(self, array_capacity, k):
        # original stack array
        self.stack_array = [None]*array_capacity
        self.k = k
        self.n = array_capacity

        # number of stacks will be the ceil value of the division.
        self.num_stacks = math.ceil(array_capacity/k)

        # store the top pointer pointing to the topmost element on the ith stack.
        self.pointers = [i - 1 for i in range(0, array_capacity, k)]
        print(f"Initialized {self.num_stacks} stacks each of {self.k} slots.")

    def push(self, stack_no, elem):
        # stack_no is 1-based indexed.
        print(f"Pushing {elem} on stack {stack_no}.")

        # get the low and high bounds of the stack.
        low = self.k * (stack_no - 1)
        high = self.k * stack_no if stack_no * self.k < self.n else self.n

        # get the current top pointer of the stack.
        top = self.pointers[stack_no - 1]

        # low - 1 would mean empty. high - 1 would mean stack is full.
        if low - 1 <= top < high - 1:
            # insert element on top + 1 index.
            self.stack_array[top + 1] = elem
            # increment the top pointer for this stack.
            self.pointers[stack_no - 1] += 1
        else:
            print(f"Overflow on stack number {stack_no}.")
        print(self.pointers, self.stack_array)

    def pop(self, stack_no):
        # stack_no is 1-based indexed.
        print(f"Popping from stack {stack_no}.")

        # get the low and high bounds of the stack.
        low = self.k * (stack_no - 1)
        high = self.k * stack_no if stack_no * self.k < self.n else self.n

        # get the current top pointer of the stack.
        top = self.pointers[stack_no - 1]

        # low - 1 means empty stack.
        if top == low - 1:
            print(f"Stack number {stack_no} is empty!")
            print(self.pointers, self.stack_array)
            return

        # get the topmost element
        item = self.stack_array[top]
        # set to None for visual perspective.
        self.stack_array[top] = None
        # decrement the top pointer.
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

stacks.pop(4)

stacks.pop(4)

stacks.push(4, 16)

stacks.push(4, 24)
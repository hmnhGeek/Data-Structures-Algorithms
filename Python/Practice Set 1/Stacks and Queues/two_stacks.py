# Problem link - https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1

class TwoStacks:
    def __init__(self):
        self.stacks = [None, None]
        self.i, self.j = 0, 1

    def push1(self, x):
        self.stacks[self.i] = x
        if self.i + 2 not in range(len(self.stacks)):
            self.stacks.append(None)
            self.stacks.append(None)
        self.i += 2

    def push2(self, x):
        self.stacks[self.j] = x
        if self.j + 2 not in range(len(self.stacks)):
            self.stacks.append(None)
            self.stacks.append(None)
        self.j += 2

    def pop1(self):
        if self.i == 0:
            return
        self.i -= 2
        item = self.stacks[self.i]
        self.stacks[self.i] = None
        return item

    def pop2(self):
        if self.j == 0:
            return
        self.j -= 2
        item = self.stacks[self.j]
        self.stacks[self.j] = None
        return item


s = TwoStacks()
s.push1(2)
s.push1(3)
s.push2(4)
print(s.pop1())
print(s.pop2())
print(s.pop2())

s = TwoStacks()
s.push1(1)
s.push2(2)
print(s.pop1())
s.push1(3)
print(s.pop1())
print(s.pop1())

s = TwoStacks()
s.push1(2)
s.push1(3)
s.push1(4)
print(s.pop2())
print(s.pop2())
print(s.pop2())

# Problem link - https://www.geeksforgeeks.org/program-for-shortest-job-first-or-sjf-cpu-scheduling-set-1-non-preemptive/
# Solution - https://www.youtube.com/watch?v=9PDUOx4MtKo


from typing import List


class Process:
    def __init__(self, pid, s, b):
        self.pid = pid
        self.start_time = s
        self.burst_time = b


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        if self.is_empty():
            return
        return self.head.data


class Solution:
    @staticmethod
    def schedule(processes: List[Process]):
        # Sort the processes by their arrival time in O(n * log(n)).
        processes.sort(key=lambda x: x.start_time)

        # get the CPU queue ready and start executing the first process.
        queue = Queue()
        queue.push(processes[0])

        # create a ready queue and push all the processes from 1 till n in O(n) time.
        ready_queue = Queue()
        for i in range(1, len(processes)):
            process = processes[i]
            ready_queue.push(process)

        # create tracking and result variables.
        wait_time = 0
        result = []

        # while CPU is working...
        while not queue.is_empty():
            # get the process and append it to the result.
            process = queue.pop()
            result.append(process)

            # update the wait time
            wait_time += process.burst_time
            next_processes = []
            while not ready_queue.is_empty() and ready_queue.front().start_time <= wait_time:
                next_processes.append(ready_queue.pop())
            next_processes.sort(key=lambda x: x.burst_time)
            for p in next_processes:
                queue.push(p)
        for process in result:
            print(process.pid, end=" ")
        print()


Solution.schedule(
    [
        Process(1, 2, 3),
        Process(2, 0, 4),
        Process(3, 4, 2),
        Process(4, 5, 4)
    ]
)

Solution.schedule(
    [
        Process(1, 2, 6),
        Process(2, 5, 2),
        Process(3, 1, 8),
        Process(4, 0, 3),
        Process(5, 4, 4)
    ]
)

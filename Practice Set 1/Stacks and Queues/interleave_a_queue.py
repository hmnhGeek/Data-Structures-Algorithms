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

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


class Solution:
    @staticmethod
    def _get_mid_node(queue: Queue) -> Node:
        counter = 0
        curr = queue.head
        while counter != queue.length // 2:
            curr = curr.next
            counter += 1
        return curr

    @staticmethod
    def interleave(queue: Queue):
        """
            Overall time complexity is O(n) and space complexity is O(n) [although the temp queue has O(1) space, but
            we are modifying the original queue, thus its space should be considered].
        """

        # if the queue length is odd, nothing can be done, return.
        if queue.length % 2 == 1:
            return

        # create a temp queue which will always hold only two elements at a time, and thus it will have a constant
        # space.
        temp_queue = Queue()

        # place `i` and `j` with i at head of the queue and j at the middle node which can be found in O(n//2) time.
        i, j = queue.head, Solution._get_mid_node(queue)

        # we need to traverse half of the queue, thus store the middle node.
        temp = j

        # while the first half has been traversed by the `i` pointer; this will take O(n//2) time.
        while i != temp.next:
            # This will take O(1) time because this queue will hold only 2 elements at a time.
            while not temp_queue.is_empty():
                queue.push(temp_queue.pop())

            # push the ith and jth node's data into the temp queue.
            temp_queue.push(i.data)
            temp_queue.push(j.data)

            # move the pointers
            i = i.next
            j = j.next

            # pop from the original queue.
            queue.pop()

        # now `j` would point to the first node in the interleaved sequence, and so, continuously pop from the queue
        # until i reaches just before j. This will take O(n//2) time.
        while i.next != j:
            queue.pop()
            i = i.next


# Example 1
q = Queue()
for i in [1, 2, 3, 4]:
    q.push(i)
q.show()
Solution.interleave(q)
q.show()

# Example 2
q = Queue()
for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    q.push(i)
q.show()
Solution.interleave(q)
q.show()

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def put_front(self, k, v):
        node = Node(k, v)
        if self.is_empty():
            # insert the node in between head and tail
            # make head's next and tail's prev to point to node.
            self.head.next = self.tail.prev = node
            # update node's pointers as well.
            node.prev = self.head
            node.next = self.tail
        else:
            # store the current first node
            temp = self.head.next
            # update the node as the first node now
            self.head.next = node
            node.prev = self.head
            # make previous first node point to this node
            temp.prev = node
            # and similarly, update the next pointer of this node to point to previous first node.
            node.next = temp
        self.length += 1
        return node

    def pop_back(self):
        if self.is_empty():
            return
        lru = self.tail.prev
        if self.length == 1:
            # if length is 1, simply connect head and tail pointers
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            # get reference to the upcoming last node
            next_lru = lru.prev
            # update the next_lru's pointers
            next_lru.next = self.tail
            self.tail.prev = next_lru
        self.length -= 1
        return lru

    def move_to_front(self, node):
        # if there is only one node, nothing needs to be done
        if self.length == 1:
            return

        # break the linkages of prev and next nodes of `node`.
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

        # this should never run though
        if self.is_empty():
            self.head.next = self.tail.prev = node
            node.prev = self.head
            node.next = self.tail
        else:
            # same logic as in the pop_back method.
            temp = self.head.next
            self.head.next = node
            node.prev = self.head
            temp.prev = node
            node.next = temp

    def show(self):
        curr = self.head
        while curr is not None:
            print(f"({curr.key}: {curr.value})", end=" ")
            curr = curr.next
        print()


class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = DoublyLinkedList()
        self.key_node_map = dict()

    def put(self, k, v):
        """
            Time complexity is O(1) and space complexity is O(1).
        """

        # if key is already present in the cache...
        if k in self.key_node_map:
            print(f"Key {k} already in cache, updating its value to {v}.")
            # get the concerned node
            node = self.key_node_map[k]
            # move it to front
            self.cache.move_to_front(node)
            # and update its value.
            node.value = v
            return

        # From here onwards, we know that k is not present in the cache.

        # now, since a new key is being inserted, let's check if the cache is full or not.
        # if it is full...
        if self.cache.length == self.capacity:
            # evict LRU
            lru = self.cache.pop_back()
            print("Cache is full, evicting LRU.")

            # erase LRU from map as well and delete LRU.
            del self.key_node_map[lru.key]
            del lru

        # finally, put the new node in front of the cache
        node = self.cache.put_front(k, v)
        # and add it into the map as well
        self.key_node_map[k] = node
        return

    def get(self, k):
        if k in self.key_node_map:
            node = self.key_node_map[k]
            self.cache.move_to_front(node)
            return node.value
        return None


# Example 1
cache = LruCache(2)
cache.put(1, 2)
print(cache.get(1))
print()

# Example 2
cache = LruCache(2)
cache.put(1, 2)
cache.put(2, 3)
cache.put(1, 5),
cache.put(4, 5)
cache.put(6, 7)
print(cache.get(4))
cache.put(1, 2)
print(cache.get(3))

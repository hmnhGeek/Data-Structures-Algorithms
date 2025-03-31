# Problem link - https://leetcode.com/problems/lru-cache/description/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def prepend(self, x):
        # This method is used to add a node 'x' to the front of the DLL.
        # This operation takes O(1) time.
        if self.head is None:
            self.push(x)
        else:
            x.next = self.head
            self.head.prev = x
            self.head = x
            self.length += 1

    def push(self, node):
        # This push method inserts at the end of the list is O(1) time.
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

    def delete(self, x):
        # This operation takes O(1) time.
        prev = x.prev
        if x == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif x == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = x.next
            x.next.prev = prev
        del x
        self.length -= 1

    def show(self):
        curr = self.head

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


class LRUCache:
    def __init__(self, capacity):
        self.cache = DoublyLinkedList()
        self.cap = capacity
        self.map = {}

    def show(self):
        print("\nThe cache is: ")
        curr = self.cache.head
        while curr is not None:
            print(curr.data[1], end=" ")
            curr = curr.next
        print()

    def put(self, key, value):
        # Overall this operation takes O(1) time.
        print(f"Putting value = {value} at key = {key}")

        # if you are trying to insert into the cache when it is full, ensure that you get the (key, value) pair
        # from the tail node which represents the least recently used node. Unpack key to lru_key. Delete the
        # tail node from the cache and delete the reference from the map as well. If cache is full and the delete
        # operation happens, then it will also take O(1).
        if self.cache.length == self.cap:
            lru_key, _ = self.cache.tail.data
            self.cache.delete(self.cache.tail)
            del self.map[lru_key]

        # create a new node and inside the node, keep a tuple value in the form (key, value).
        # We will see how this is useful.
        node = Node((key, value))

        # if the key already exists in our map, ensure that you delete the node represented
        # by that key. The node is self.map[key]. We delete it from the cache. This operation
        # takes O(1) time.
        if key in self.map:
            self.cache.delete(self.map[key])

        # now, we assign the newly created node with (key, value) as its data and add it to our map.
        # Basically, the map holds the node reference at key. If the key was already present in the
        # map, it will just update the reference with that of the new node, otherwise a new key will
        # be created.
        self.map[key] = node

        # once the map is updated, ensure that the new node is prepended into the cache, as this
        # will be the most significant node now. This operation takes O(1) time.
        self.cache.prepend(node)

    def get(self, key):
        print("Getting value at key = ", key)
        # check if the key is present in the map.
        if key in self.map:
            # extract the node from the map which is represented by the key.
            old = self.map[key]

            # create a new node with same key value pair
            new_node = Node((key, old.data[1]))

            # delete the old node from the cache in O(1) time.
            self.cache.delete(old)

            # update the new node in the map.
            self.map[key] = new_node

            # prepend the new node in the cache in O(1) time.
            self.cache.prepend(new_node)

            return self.map[key].data[1]
        else:
            # if key is not in map, then it is not in cache as well.
            return -1


l = LRUCache(3)
l.put(1, 'A')
l.show()
l.put(2, 'B')
l.show()
l.put(3, "C")
l.show()
print(l.get(2))
l.show()
print(l.get(4))
l.show()
l.put(4, "D")
l.show()
l.put(3, "E")
l.show()
print(l.get(4))
l.show()
l.put(1, "A")
l.show()
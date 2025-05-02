class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

class Solution:
    @staticmethod
    def get_height(root: Node):
        if root is None:
            return 0
        return 1 + max(Solution.get_height(root.left), Solution.get_height(root.right))
    

# Example 1
one, two, three = Node(1), Node(2), Node(3)
one.left = two
one.right = three
print(Solution.get_height(one))

# Example 2
one, two, three = Node(1), Node(2), Node(3)
two.right = one
one.left = three
print(Solution.get_height(two))

# Example 3
n12, n8, n18, n5, n11 = Node(12), Node(8), Node(18), Node(5), Node(11)
n12.left = n8
n8.left = n5
n12.right = n18
n8.right = n11
print(Solution.get_height(n12))

# Example 4
n1, n2, n3, n4, n5, n6, n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
n1.left = n2
n2.left = n4
n5.left = n6
n1.right = n3
n3.right = n5
n5.right = n7
print(Solution.get_height(n1))

# Example 5
n1, n2, n5, n4, n6, n55 = Node(1), Node(2), Node(5), Node(4), Node(6), Node(5)
n1.left = n2
n5.left = n4
n4.left = n55
n1.right = n5
n5.right = n6
print(Solution.get_height(n1))
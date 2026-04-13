# Problem link - https://www.geeksforgeeks.org/problems/transform-to-sum-tree/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def convert_to_sum_tree(node):
        """
            Time complexity is O(n) and space complexity is O(h).
        """
        if node is None:
            return 0
        data = node.data
        ld = Solution.convert_to_sum_tree(node.left)
        rd = Solution.convert_to_sum_tree(node.right)
        node.data = ld + rd
        return node.data + data


def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.data, end=" ")
    print_tree(node.right)


# Create solution object
sol = Solution()

# -------- First Tree --------
# Create nodes
n10 = Node(10)
n_2 = Node(-2)
n6 = Node(6)
n8 = Node(8)
n_4 = Node(-4)
n7 = Node(7)
n5 = Node(5)

# Connect nodes
n10.left = n_2
n10.right = n6

n_2.left = n8
n_2.right = n_4

n6.left = n7
n6.right = n5

# Print original tree
print("Original Tree:")
print_tree(n10)

# Convert to sum tree
sol.convert_to_sum_tree(n10)

# Print transformed tree
print("\nSum Tree:")
print_tree(n10)

print("\n\n")


# -------- Second Tree --------
# Create nodes
n5 = Node(5)
n1 = Node(1)
n_8 = Node(-8)
n4 = Node(4)
n6 = Node(6)

# Connect nodes
n5.right = n1

n1.left = n_8
n1.right = n4

n_8.left = n6

# Print original tree
print("Original Tree:")
print_tree(n5)

# Convert to sum tree
sol.convert_to_sum_tree(n5)

# Print sum tree
print("\nSum Tree:")
print_tree(n5)

print("\n\n")


# -------- Third Tree --------
# Create nodes
n1_root = Node(1)
n_2 = Node(-2)
n1_right = Node(1)
n3 = Node(3)
n1_leaf = Node(1)

# Connect nodes
n1_root.left = n_2
n1_root.right = n1_right

n_2.left = n3
n_2.right = n1_leaf

# Print original tree
print("Original Tree:")
print_tree(n1_root)

# Convert to sum tree
sol.convert_to_sum_tree(n1_root)

# Print sum tree
print("\nSum Tree:")
print_tree(n1_root)
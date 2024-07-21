class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def recursive():
    def h(node: Node):
        '''This function is used to ignore the node's data into sum.'''

        # if node is None, return 0
        if node is None:
            return 0

        # if node is a leaf node, then also return 0 as you're not considering the node.
        if node.left is None and node.right is None:
            return 0

        # if you're not considering a node, there will be four recursions possible
        # RECURSION 1: You consider the left child in sum
        # RECURSION 2: You don't consider the left child in sum
        # RECURSION 3: You consider the right child in sum
        # RECURSION 4: You don't consider the right child in the sum
        # Since in this case we have 4 options to choose from, we will
        # do a max() call to find the maximum sums that we might get from
        # these 4 recursive calls. Also, please node that we are not adding node's data
        # as we are not considering this node.
        return max(
            f(node.left) + f(node.right),
            h(node.left) + h(node.right),
            f(node.left) + h(node.right),
            h(node.left) + f(node.right)
        )


    def f(node: Node):
        '''This function is used to consider the node's data into sum.'''

        # if the node is None, return 0
        if node is None:
            return 0

        # if the node is a leaf node, return the node's data as this node is
        # being considered in the sum
        if node.left is None and node.right is None:
            return node.data

        # if you're considering the node, you cannot consider its children
        # since node is not a leaf node, you must return node's data
        # plus whatever sums are obtained by not considering the children
        # please note that we are adding h(left) and h(right) and not
        # max(h(left), h(right)), because when you don't consider children,
        # you can have nodes from both left and right subtrees, so taking
        # a max would have decreased the sum.
        return node.data + h(node.left) + h(node.right)


    def g(node: Node):
        # for a given root node, we can have two recursive calls
        # let function f return the sum when root node is considered
        # let function h return the sum when root node is not considered
        # out of the two, function g will return the maximum sum.
        return max(f(node), h(node))


    def example1():
        one, two, three, one1, four, five = Node(1), Node(2), Node(3), Node(1), Node(4), Node(5)
        one.left = two
        two.left = one1
        three.left = four

        one.right = three
        three.right = five

        print(g(one))


    def example2():
        one, two, three, one1, one2, four, five = Node(1), Node(2), Node(3), Node(1), Node(1), Node(4), Node(5)
        one.left = two
        two.left = one1
        three.left = four

        one.right = three
        three.right = five
        two.right = one2

        print(g(one))


    def example3():
        two, six, eight, zero, nine1, nine2, seven = Node(2), Node(6), Node(8), Node(0), Node(9), Node(9), Node(7)

        two.left = zero
        eight.left = seven

        two.right = six
        six.right = eight
        eight.right = nine1
        nine1.right = nine2

        print(g(two))


    def example4():
        eight, hundered, mfive, thone, eione, sixsix, eifive, mten = Node(8), Node(100), Node(-5), Node(31), Node(81), Node(66), Node(85), Node(-10)

        eight.left = hundered
        hundered.left = thone
        sixsix.left = eifive

        eight.right = mfive
        mfive.right = sixsix
        sixsix.right = mten
        hundered.right = eione

        print(g(eight))

    def example5():
        fourtyone = Node(41)
        m100 = Node(-100)
        twtytwo = Node(22)
        sixteen = Node(16)
        fiftyfive = Node(55)
        m15 = Node(-15)
        ninetytwo = Node(92)
        fourty = Node(40)
        fifty = Node(50)

        fourtyone.left = m100
        m100.left = sixteen
        twtytwo.left = m15
        m15.left = fifty

        fourtyone.right = twtytwo
        twtytwo.right = ninetytwo
        m100.right = fiftyfive
        sixteen.right = fourty

        print(g(fourtyone))

    print("Example 1")
    example1()

    print()
    print("Example 2")
    example2()

    print()
    print("Example 3")
    example3()

    print()
    print("Example 4")
    example4()

    print()
    print("Example 5")
    example5()


def memoized():
    def h(node: Node, dp):
        '''This function is used to ignore the node's data into sum.'''

        # if node is None, return 0
        if node is None:
            return 0

        # if node is a leaf node, then also return 0 as you're not considering the node.
        if node.left is None and node.right is None:
            return 0

        if dp[node]["not_take"] is not None:
            return dp[node]["not_take"]

        # if you're not considering a node, there will be four recursions possible
        # RECURSION 1: You consider the left child in sum
        # RECURSION 2: You don't consider the left child in sum
        # RECURSION 3: You consider the right child in sum
        # RECURSION 4: You don't consider the right child in the sum
        # Since in this case we have 4 options to choose from, we will
        # do a max() call to find the maximum sums that we might get from
        # these 4 recursive calls. Also, please node that we are not adding node's data
        # as we are not considering this node.
        dp[node]["not_take"] = max(
            f(node.left, dp) + f(node.right, dp),
            h(node.left, dp) + h(node.right, dp),
            f(node.left, dp) + h(node.right, dp),
            h(node.left, dp) + f(node.right, dp)
        )
        return dp[node]["not_take"]


    def f(node: Node, dp):
        '''This function is used to consider the node's data into sum.'''

        # if the node is None, return 0
        if node is None:
            return 0

        # if the node is a leaf node, return the node's data as this node is
        # being considered in the sum
        if node.left is None and node.right is None:
            return node.data

        if dp[node]["take"] is not None:
            return dp[node]["take"]

        # if you're considering the node, you cannot consider its children
        # since node is not a leaf node, you must return node's data
        # plus whatever sums are obtained by not considering the children
        # please note that we are adding h(left) and h(right) and not
        # max(h(left), h(right)), because when you don't consider children,
        # you can have nodes from both left and right subtrees, so taking
        # a max would have decreased the sum.
        dp[node]["take"] = node.data + h(node.left, dp) + h(node.right, dp)
        return dp[node]["take"]


    def g(node: Node, nodes):
        dp = {i: {"take": None, "not_take": None} for i in nodes}

        # for a given root node, we can have two recursive calls
        # let function f return the sum when root node is considered
        # let function h return the sum when root node is not considered
        # out of the two, function g will return the maximum sum.
        ans = max(f(node, dp), h(node, dp))
        for i in dp:
            print(i, dp[i])
        return ans


    def example1():
        one, two, three, one1, four, five = Node(1), Node(2), Node(3), Node(1), Node(4), Node(5)
        one.left = two
        two.left = one1
        three.left = four

        one.right = three
        three.right = five

        print(g(one, [one, two, three, one1, four, five]))


    def example2():
        one, two, three, one1, one2, four, five = Node(1), Node(2), Node(3), Node(1), Node(1), Node(4), Node(5)
        one.left = two
        two.left = one1
        three.left = four

        one.right = three
        three.right = five
        two.right = one2

        print(g(one, [one, two, three, one1, one2, four, five]))


    def example3():
        two, six, eight, zero, nine1, nine2, seven = Node(2), Node(6), Node(8), Node(0), Node(9), Node(9), Node(7)

        two.left = zero
        eight.left = seven

        two.right = six
        six.right = eight
        eight.right = nine1
        nine1.right = nine2

        print(g(two, [two, six, eight, zero, nine1, nine2, seven]))


    def example4():
        eight, hundered, mfive, thone, eione, sixsix, eifive, mten = Node(8), Node(100), Node(-5), Node(31), Node(81), Node(66), Node(85), Node(-10)

        eight.left = hundered
        hundered.left = thone
        sixsix.left = eifive

        eight.right = mfive
        mfive.right = sixsix
        sixsix.right = mten
        hundered.right = eione

        print(g(eight, [eight, hundered, mfive, thone, eione, sixsix, eifive, mten]))

    def example5():
        fourtyone = Node(41)
        m100 = Node(-100)
        twtytwo = Node(22)
        sixteen = Node(16)
        fiftyfive = Node(55)
        m15 = Node(-15)
        ninetytwo = Node(92)
        fourty = Node(40)
        fifty = Node(50)

        fourtyone.left = m100
        m100.left = sixteen
        twtytwo.left = m15
        m15.left = fifty

        fourtyone.right = twtytwo
        twtytwo.right = ninetytwo
        m100.right = fiftyfive
        sixteen.right = fourty

        print(g(fourtyone, [fourtyone, m100, twtytwo, sixteen, fiftyfive, m15, ninetytwo, fourty, fifty]))

    print("Example 1")
    example1()

    print()
    print("Example 2")
    example2()

    print()
    print("Example 3")
    example3()

    print()
    print("Example 4")
    example4()

    print()
    print("Example 5")
    example5()



memoized()
package BinaryTrees.Problem18;


class Node<T> {
    public T data;
    public Node<T> left;
    public Node<T> right;

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
    }
}


class TraversalTracker<T> {
    public Node<T> prev, curr, head, tail;

    public TraversalTracker(Node<T> prev, Node<T> curr) {
        this.prev = prev;
        this.curr = curr;
    }
}


public class Solution {
    public static <T> void convertBtToDll(TraversalTracker<T> traversalTracker) {
        if (traversalTracker.curr == null) return;

        Node<T> prevCurr = traversalTracker.curr;
        traversalTracker.curr = traversalTracker.curr.left;
        convertBtToDll(traversalTracker);
        traversalTracker.curr = prevCurr;

        if (traversalTracker.prev == null) {
            traversalTracker.head = traversalTracker.curr;
        } else {
            traversalTracker.curr.left = traversalTracker.prev;
            traversalTracker.prev.right = traversalTracker.curr;
        }
        traversalTracker.prev = traversalTracker.curr;

        prevCurr = traversalTracker.curr;
        traversalTracker.curr = traversalTracker.curr.right;
        convertBtToDll(traversalTracker);
        traversalTracker.curr = prevCurr;
    }

    private static <T> Node<T> getLeftmostLeaf(Node<T> root) {
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }

    public static void main(String[] args) {
        // Example 1
        Node<Integer> node3 = new Node<>(3), node5 = new Node<>(5), node2 = new Node<>(2),
                node1 = new Node<>(1), node4 = new Node<>(4), node6 = new Node<>(6);
        node3.left = node5;
        node3.right = node2;
        node2.left = node1;
        node1.left = node4;
        node1.right = node6;
        Node<Integer> head = getLeftmostLeaf(node3);
        convertBtToDll(new TraversalTracker<>(null, node3));
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.right;
        }
        System.out.println();
    }
}

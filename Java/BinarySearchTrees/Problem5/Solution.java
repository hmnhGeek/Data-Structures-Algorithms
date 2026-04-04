package BinarySearchTrees.Problem5;

public class Solution {
    private static <T extends Comparable<T>> Boolean isBst(Node<T> node, T low, T high) {
        if (node == null) return Boolean.TRUE;
        if (!(low.compareTo(node.data) <= 0 && high.compareTo(node.data) >= 0)) return Boolean.FALSE;
        Boolean leftSubtreeIsBst = isBst(node.left, low, node.data);
        Boolean rightSubtreeIsBst = isBst(node.right, node.data, high);
        return leftSubtreeIsBst && rightSubtreeIsBst;
    }

    public static Boolean isBst(Node<Integer> root) {
        return isBst(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    public static void main(String[] args) {

        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n5 = new Node<>(5);

        n2.left = n1;
        n2.right = n3;
        n3.right = n5;

        System.out.println(Solution.isBst(n2)); // true


        // Example 2
        Node<Integer> a2 = new Node<>(2);
        Node<Integer> a6 = new Node<>(6);
        Node<Integer> a7 = new Node<>(7);
        Node<Integer> a9 = new Node<>(9);

        a2.right = a7;
        a7.right = a6; // invalid BST
        a6.right = a9;

        System.out.println(Solution.isBst(a2)); // false


        // Example 3
        Node<Integer> b10 = new Node<>(10);
        Node<Integer> b5 = new Node<>(5);
        Node<Integer> b20 = new Node<>(20);
        Node<Integer> b9 = new Node<>(9);
        Node<Integer> b25 = new Node<>(25);

        b10.left = b5;
        b10.right = b20;
        b20.left = b9; // invalid placement
        b20.right = b25;

        System.out.println(Solution.isBst(b10)); // false


        // Example 4
        Node<Integer> c1 = new Node<>(1);
        Node<Integer> c4 = new Node<>(4);
        Node<Integer> c5 = new Node<>(5);
        Node<Integer> c3 = new Node<>(3);
        Node<Integer> c6 = new Node<>(6);

        c5.left = c1;
        c5.right = c4; // invalid (4 < 5 but on right)
        c4.left = c3;
        c4.right = c6;

        System.out.println(Solution.isBst(c5)); // false


        // Example 5
        Node<Integer> d1 = new Node<>(1);
        Node<Integer> d2 = new Node<>(2);
        Node<Integer> d3 = new Node<>(3);

        d2.left = d1;
        d2.right = d3;

        System.out.println(Solution.isBst(d2)); // true
    }
}

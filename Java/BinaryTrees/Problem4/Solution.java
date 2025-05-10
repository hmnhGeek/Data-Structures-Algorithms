package BinaryTrees.Problem4;

public class Solution {
    private static <T> Integer getHeight(Node<T> root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(getHeight(root.getLeft()), getHeight(root.getRight()));
    }

    public static <T> Integer getDiameter(Node<T> root) {
        return 1 + getHeight(root.getLeft()) + getHeight(root.getRight());
    }

    public static void main(String[] args) {
        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        n1.setLeft(n2);
        n1.setRight(n3);
        System.out.println(getDiameter(n1));
    }
}

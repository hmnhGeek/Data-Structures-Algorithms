package BinaryTrees.Problem26;


class Node<T> {
    public T data;
    public Node<T> left, right;

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
    }
}


class Vector {
    public Integer height;
    public Integer sum;

    public Vector(Integer height, Integer sum) {
        this.height = height;
        this.sum = sum;
    }
}


public class Solution {
    public static Integer getMaxPathSum(Node<Integer> root) {
        Vector vector = solve(root);
        return vector.sum;
    }

    private static Vector solve(Node<Integer> root) {
        if (root == null) return new Vector(0, 0);
        Vector left = solve(root.left);
        Vector right = solve(root.right);
        if (left.height > right.height) {
            return new Vector(left.height + 1, left.sum + root.data);
        } else if (left.height < right.height) {
            return new Vector(right.height + 1, right.sum + root.data);
        } else {
            return new Vector(left.height + 1, Math.max(left.sum, right.sum) + root.data);
        }
    }

    public static void main(String[] args) {
        // Root
        Node<Integer> root = new Node<>(4);

        // Level 1
        root.left = new Node<>(2);
        root.right = new Node<>(5);

        // Level 2
        root.left.left = new Node<>(7);
        root.left.right = new Node<>(1);

        root.right.left = new Node<>(2);
        root.right.right = new Node<>(3);

        // Level 3
        root.left.right.left = new Node<>(6);

        // Find maximum path sum
        System.out.println(getMaxPathSum(root));
    }
}

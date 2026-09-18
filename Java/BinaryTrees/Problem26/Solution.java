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

        // =========================
        // Tree 1
        // =========================
        //
        //          4
        //        /   \
        //       2     5
        //      / \   / \
        //     7   1 2   3
        //        /
        //       6

        Node<Integer> root1 = new Node<>(4);

        root1.left = new Node<>(2);
        root1.right = new Node<>(5);

        root1.left.left = new Node<>(7);
        root1.left.right = new Node<>(1);

        root1.right.left = new Node<>(2);
        root1.right.right = new Node<>(3);

        root1.left.right.left = new Node<>(6);

        System.out.println("Tree 1 Max Path Sum: " + getMaxPathSum(root1));


        // =========================
        // Tree 2
        // =========================
        //
        //          1
        //        /   \
        //       2     3
        //      / \   / \
        //     4   5 6   7

        Node<Integer> root2 = new Node<>(1);

        root2.left = new Node<>(2);
        root2.right = new Node<>(3);

        root2.left.left = new Node<>(4);
        root2.left.right = new Node<>(5);

        root2.right.left = new Node<>(6);
        root2.right.right = new Node<>(7);

        System.out.println("Tree 2 Max Path Sum: " + getMaxPathSum(root2));


        // =========================
        // Tree 3
        // =========================
        //
        //          10
        //        /    \
        //       5      15
        //      / \       \
        //     3   7       20
        //    /
        //   1

        Node<Integer> root3 = new Node<>(10);

        root3.left = new Node<>(5);
        root3.right = new Node<>(15);

        root3.left.left = new Node<>(3);
        root3.left.right = new Node<>(7);

        root3.left.left.left = new Node<>(1);

        root3.right.right = new Node<>(20);

        System.out.println("Tree 3 Max Path Sum: " + getMaxPathSum(root3));
    }
}

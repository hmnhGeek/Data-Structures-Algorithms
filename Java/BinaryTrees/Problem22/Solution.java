package BinaryTrees.Problem22;


class Result {
    public Integer sum;
    public boolean flag;

    public Result(Integer sum, boolean flag) {
        this.sum = sum;
        this.flag = flag;
    }
}


public class Solution {
    public static Boolean isBTSumTree(Node<Integer> root) {
        Result result = isSumTree(root);
        return result.flag;
    }

    private static Result isSumTree(Node<Integer> root) {
        if (root == null) return new Result(0, true);
        if (root.left == null && root.right == null) return new Result(root.data, true);
        Result leftResult = isSumTree(root.left);
        Result rightResult = isSumTree(root.right);
        if (leftResult.sum + rightResult.sum == root.data) {
            return new Result(leftResult.sum + rightResult.sum + root.data, true);
        }
        return new Result(0, false);
    }

    public static void main(String[] args) {

        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);

        n3.left = n1;
        n3.right = n2;

        System.out.println(Solution.isBTSumTree(n3));


        // Example 2
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n20 = new Node<>(20);
        Node<Integer> n30 = new Node<>(30);
        Node<Integer> n101 = new Node<>(10);
        Node<Integer> n102 = new Node<>(10);

        n10.left = n20;
        n10.right = n30;
        n20.left = n101;
        n20.right = n102;

        System.out.println(Solution.isBTSumTree(n10));


        // Example 3
        Node<Integer> a26 = new Node<>(26);
        Node<Integer> a10 = new Node<>(10);
        Node<Integer> a3 = new Node<>(3);
        Node<Integer> a4 = new Node<>(4);
        Node<Integer> a6 = new Node<>(6);
        Node<Integer> a31 = new Node<>(3);

        a26.left = a10;
        a26.right = a3;
        a10.left = a4;
        a10.right = a6;
        a3.right = a31;

        System.out.println(Solution.isBTSumTree(a26));


        // Example 4
        Node<Integer> b26 = new Node<>(26);
        Node<Integer> b10 = new Node<>(10);
        Node<Integer> b3 = new Node<>(3);
        Node<Integer> b2 = new Node<>(2);
        Node<Integer> b6 = new Node<>(6);
        Node<Integer> b31 = new Node<>(3);

        b26.left = b10;
        b26.right = b3;
        b10.left = b2;
        b10.right = b6;
        b3.right = b31;

        System.out.println(Solution.isBTSumTree(b26));


        // Example 5
        Node<Integer> c1 = new Node<>(1);
        Node<Integer> c2 = new Node<>(2);
        Node<Integer> c3 = new Node<>(3);

        c3.right = c1;
        c1.left = c2;

        System.out.println(Solution.isBTSumTree(c3));
    }
}

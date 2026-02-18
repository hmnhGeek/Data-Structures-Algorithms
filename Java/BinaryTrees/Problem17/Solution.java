package BinaryTrees.Problem17;

public class Solution {
    private static Integer i = 0;

    public static void main(String[] args) {
        // Example 1
        Node<Integer> tree1 = getBinaryTree("1(2)(3)" );
        printInorder(tree1);
        System.out.println();
    }

    private static <T> void printInorder(Node<T> node) {
        if (node != null) {
            printInorder(node.left);
            System.out.println(node.data);
            printInorder(node.right);
        }
    }

    public static Node<Integer> getBinaryTree(String s) {
        i = 0;
        Node<Integer> root = new Node<>(null);
        solve(root, s);
        return root;
    }

    private static void solve(Node<Integer> root, String s) {
        if (i < s.length() && Character.isDigit(s.charAt(i))) {
            int sum = 0;
            while (i < s.length() && Character.isDigit(s.charAt(i))) {
                sum *= 10;
                sum += Integer.parseInt(String.valueOf(s.charAt(i)));
                i += 1;
            }
            root.data = sum;
        }
        if (i < s.length() && String.valueOf(s.charAt(i)).equals("(")) {
            root.left = new Node<>(null);
            i += 1;
            solve(root.left, s);
        }
        if (i < s.length() && String.valueOf(s.charAt(i)).equals("(")) {
            root.right = new Node<>(null);
            i += 1;
            solve(root.right, s);
        }
        if (i >= s.length() || String.valueOf(s.charAt(i)).equals(")")) {
            i += 1;
            return;
        }
    }
}

// Problem link - https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/

package BinaryTrees.Problem6;

import java.util.ArrayList;
import java.util.List;

class TreeNode<T> {
    private T data;
    private TreeNode<T> left;
    private TreeNode<T> right;

    public TreeNode(T data) {
        this.data = data;
        this.left = this.right = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public TreeNode<T> getLeft() {
        return left;
    }

    public void setLeft(TreeNode<T> left) {
        this.left = left;
    }

    public TreeNode<T> getRight() {
        return right;
    }

    public void setRight(TreeNode<T> right) {
        this.right = right;
    }
}

public class Solution {
    public static <T> List<T> getInorderIterative(TreeNode<T> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Stack<TreeNode<T>> stack = new Stack<>();
        TreeNode<T> curr = root;
        List<T> result = new ArrayList<>();
        while (curr != null) {
            stack.push(curr);
            curr = curr.getLeft();
        }
        while (!stack.isEmpty()) {
            TreeNode<T> treeNode = stack.pop();
            result.add(treeNode.getData());
            TreeNode<T> temp = treeNode.getRight();
            while (temp != null) {
                stack.push(temp);
                temp = temp.getLeft();
            }
        }
        return result;
    }

    public static <T> void getInorder(TreeNode<T> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        if (root != null) {
            getInorder(root.getLeft());
            System.out.println(root.getData());
            getInorder(root.getRight());
        }
    }

    public static void main(String[] args) {
        // Example 1
        TreeNode<Integer> n1 = new TreeNode<>(1);
        TreeNode<Integer> n2 = new TreeNode<>(2);
        TreeNode<Integer> n3 = new TreeNode<>(3);
        TreeNode<Integer> n4 = new TreeNode<>(4);
        TreeNode<Integer> n5 = new TreeNode<>(5);
        TreeNode<Integer> n6 = new TreeNode<>(6);
        TreeNode<Integer> n7 = new TreeNode<>(7);
        TreeNode<Integer> n8 = new TreeNode<>(8);
        n1.setLeft(n2);
        n2.setLeft(n4);
        n1.setRight(n3);
        n3.setLeft(n5);
        n3.setRight(n6);
        n5.setLeft(n7);
        n5.setRight(n8);
        System.out.println(getInorderIterative(n1));
        getInorder(n1);

        // Example 2
        TreeNode<Character> a = new TreeNode<>('a');
        TreeNode<Character> b = new TreeNode<>('b');
        TreeNode<Character> c = new TreeNode<>('c');
        TreeNode<Character> d = new TreeNode<>('d');
        a.setLeft(b);
        a.setRight(c);
        c.setLeft(d);
        System.out.println(getInorderIterative(a));
        getInorder(a);
    }
}

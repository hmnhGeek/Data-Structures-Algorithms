// Problem link - https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1
// Solution - https://www.youtube.com/watch?v=KV4mRzTjlAk


package BinaryTrees.Problem9;

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

class Element<T> {
    public T data;
    public Integer level;

    public Element(T data, Integer level) {
        this.data = data;
        this.level = level;
    }
}

public class Solution {
    public static void main(String[] args) {
        // Example 1
        TreeNode<Integer> root = new TreeNode<>(1);

        TreeNode<Integer> node2 = new TreeNode<>(2);
        TreeNode<Integer> node3 = new TreeNode<>(3);

        TreeNode<Integer> node4 = new TreeNode<>(4);
        TreeNode<Integer> node5 = new TreeNode<>(5);
        TreeNode<Integer> node6 = new TreeNode<>(6);
        TreeNode<Integer> node7 = new TreeNode<>(7);

        // Connecting nodes as per the tree diagram
        root.setLeft(node2);
        root.setRight(node3);
        node2.setLeft(node4);
        node2.setRight(node5);
        node5.setLeft(node6);
        node3.setRight(node7);
        System.out.println(getLeftView(root));

        TreeNode<Integer> root1 = new TreeNode<>(1);

        TreeNode<Integer> node21 = new TreeNode<>(2);
        TreeNode<Integer> node31 = new TreeNode<>(3);
        TreeNode<Integer> node41 = new TreeNode<>(4);
        TreeNode<Integer> node51 = new TreeNode<>(5);

        // Connecting nodes as per the tree diagram
        root1.setLeft(node21);
        root1.setRight(node31);
        node31.setLeft(node41);
        node41.setRight(node51);
        System.out.println(getLeftView(root1));
    }

    public static <T> List<T> getLeftView(TreeNode<T> root) {
        Queue<Element<TreeNode<T>>> queue = new Queue<>();
        queue.push(new Element<>(root, 0));
        Integer counter = 0;
        List<T> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            Element<TreeNode<T>> element = queue.pop();
            if (counter == element.level) {
                result.add(element.data.getData());
                counter += 1;
            }
            if (element.data.getLeft() != null) {
                queue.push(new Element<>(element.data.getLeft(), element.level + 1));
            }
            if (element.data.getRight() != null) {
                queue.push(new Element<>(element.data.getRight(), element.level + 1));
            }
        }
        return result;
    }
}

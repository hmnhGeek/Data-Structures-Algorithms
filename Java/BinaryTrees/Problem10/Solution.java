// Problem link - https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1


package BinaryTrees.Problem10;


import BinaryTrees.Problem10.Queue.Queue;

import java.util.ArrayList;
import java.util.List;

class Node<T> {
    private T data;
    private Node<T> left;
    private Node<T> right;

    public Node(T data) {
        this.data = data;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getLeft() {
        return left;
    }

    public void setLeft(Node<T> left) {
        this.left = left;
    }

    public Node<T> getRight() {
        return right;
    }

    public void setRight(Node<T> right) {
        this.right = right;
    }
}


class QueueElement<T> {
    public Node<T> node;
    public Integer level;

    public QueueElement(Node<T> node, Integer level) {
        this.node = node;
        this.level = level;
    }
}


public class Solution {
    public static <T> List<T> getRightView(Node<T> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Queue<QueueElement<T>> queue = new Queue<>();
        queue.push(new QueueElement<>(root, 0));
        Integer currentLevel = 0;
        List<T> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            QueueElement<T> queueElement = queue.pop();
            if (currentLevel.equals(queueElement.level)) {
                result.add(queueElement.node.getData());
                currentLevel += 1;
            }
            Node<T> node = queueElement.node;
            if (node.getRight() != null) {
                queue.push(new QueueElement<>(node.getRight(), queueElement.level + 1));
            }
            if (node.getLeft() != null) {
                queue.push(new QueueElement<>(node.getLeft(), queueElement.level + 1));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        // -------- Example 1 --------
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n4 = new Node<>(4);
        Node<Integer> n5 = new Node<>(5);
        Node<Integer> n6 = new Node<>(6);
        Node<Integer> n7 = new Node<>(7);
        Node<Integer> n8 = new Node<>(8);

        n1.setLeft(n2);
        n2.setLeft(n4);
        n3.setLeft(n6);
        n1.setRight(n3);
        n3.setRight(n7);
        n2.setRight(n5);
        n4.setRight(n8);

        System.out.println("Right view (Example 1): " + getRightView(n1));

        // -------- Example 2 --------
        Node<Integer> m1 = new Node<>(1);
        Node<Integer> m2 = new Node<>(2);
        Node<Integer> m3 = new Node<>(3);

        m1.setLeft(m3);
        m1.setRight(m2);

        System.out.println("Right view (Example 2): " + getRightView(m1));

        // -------- Example 3 --------
        Node<Integer> o10 = new Node<>(10);
        Node<Integer> o20 = new Node<>(20);
        Node<Integer> o30 = new Node<>(30);
        Node<Integer> o40 = new Node<>(40);
        Node<Integer> o60 = new Node<>(60);

        o10.setLeft(o20);
        o20.setLeft(o40);
        o10.setRight(o30);
        o20.setRight(o60);

        System.out.println("Right view (Example 3): " + getRightView(o10));
    }
}

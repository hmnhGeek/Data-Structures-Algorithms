// Problem link - https://www.geeksforgeeks.org/problems/reverse-level-order-traversal/1

package BinaryTrees.Problem2;


import java.util.ArrayList;
import java.util.List;

class QueueNode<T> {
    private T data;
    private QueueNode<T> next;

    public QueueNode(T data) {
        this.data = data;
        this.next = null;
    }

    public QueueNode<T> getNext() {
        return next;
    }

    public void setNext(QueueNode<T> next) {
        this.next = next;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }
}


class Queue<T> {
    private QueueNode<T> head;
    private QueueNode<T> tail;
    private Integer length;

    public Queue() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        QueueNode<T> node = new QueueNode<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.setNext(node);
            this.tail = node;
        }
        this.length += 1;
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = this.head.getData();
        this.head = this.head.getNext();
        this.length -= 1;
        return item;
    }
}


class Node<T> {
    private T data;
    private Node<T> left;
    private Node<T> right;

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
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

    public T getData() {
        return data;
    }
}


class Solution {
    public static void main(String[] args) {
        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        n1.setLeft(n3);
        n1.setRight(n2);
        System.out.println(getReverseOrderTraversal(n1));

        // Example 2
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n20 = new Node<>(20);
        Node<Integer> n30 = new Node<>(30);
        Node<Integer> n40 = new Node<>(40);
        Node<Integer> n60 = new Node<>(60);
        n10.setLeft(n20);
        n10.setRight(n30);
        n20.setLeft(n40);
        n20.setRight(n60);
        System.out.println(getReverseOrderTraversal(n10));
    }

    public static <T> List<T> getReverseOrderTraversal(Node<T> root) {
        /**
         * Time complexity is O(n) and space complexity is O(n).
         */

        // define a blank queue and push root node into it.
        Queue<Node<T>> queue = new Queue<>();
        queue.push(root);

        // define a result list.
        List<T> result = new ArrayList<>();

        // typical BFS...
        while (!queue.isEmpty()) {
            Node<T> node = queue.pop();

            // add the popped node's data into the result list.
            result.add(node.getData());

            // add right node first, then left node into the queue.
            // We check right first because in the reversed order we want to see left child first.
            if (node.getRight() != null) {
                queue.push(node.getRight());
            }
            if (node.getLeft() != null) {
                queue.push(node.getLeft());
            }
        }

        // return the reversed result for the final answer in O(n) time.
        return result.reversed();
    }
}
package BinaryTrees;

import java.util.ArrayList;
import java.util.List;

class QueueNode<T> {
    public T getData() {
        return data;
    }

    public QueueNode<T> getNext() {
        return next;
    }

    private T data;
    private QueueNode<T> next;

    public QueueNode(T data) {
        this.data = data;
        this.next = null;
    }

    public void setNext(QueueNode<T> next) {
        this.next = next;
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
        return length == 0;
    }

    public void push(T x) {
        QueueNode<T> node = new QueueNode<>(x);
        if (isEmpty()) {
            head = tail = node;
        }
        else {
            tail.setNext(node);
            tail = node;
        }
        length += 1;
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = head.getData();
        head = head.getNext();
        length -= 1;
        return item;
    }
}


class Node<T> {
    private T data;
    private Node<T> left;
    private Node<T> right;

    public void setLeft(Node<T> left) {
        this.left = left;
    }

    public void setRight(Node<T> right) {
        this.right = right;
    }

    public T getData() {
        return data;
    }

    public Node<T> getLeft() {
        return left;
    }

    public Node<T> getRight() {
        return right;
    }

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
    }
}


class Solution {
    public static void main(String[] args) {
        // Example 1
        Node<Integer> node1 = new Node<>(1);
        Node<Integer> node2 = new Node<>(2);
        Node<Integer> node3 = new Node<>(3);
        node1.setLeft(node2);
        node1.setRight(node3);
        System.out.println(getLevelOrderTraversal(node1));

        // Example 2
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n20 = new Node<>(20);
        Node<Integer> n30 = new Node<>(30);
        Node<Integer> n40 = new Node<>(40);
        Node<Integer> n50 = new Node<>(50);
        n10.setLeft(n20);
        n10.setRight(n30);
        n20.setLeft(n40);
        n20.setRight(n50);
        System.out.println(getLevelOrderTraversal(n10));

        // Example 3
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n4 = new Node<>(4);
        Node<Integer> n5 = new Node<>(5);
        Node<Integer> n6 = new Node<>(6);
        n1.setLeft(n3);
        n1.setRight(n2);
        n2.setRight(n4);
        n4.setLeft(n6);
        n4.setRight(n5);
        System.out.println(getLevelOrderTraversal(n1));
    }

    public static <T> List<T> getLevelOrderTraversal(Node<T> root) {
        Queue<Node<T>> queue = new Queue<>();
        queue.push(root);
        List<T> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            Node<T> node = queue.pop();
            result.add(node.getData());
            if (node.getLeft() != null) {
                queue.push(node.getLeft());
            }
            if (node.getRight() != null) {
                queue.push(node.getRight());
            }
        }
        return result;
    }
}
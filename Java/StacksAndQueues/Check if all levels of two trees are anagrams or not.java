package StacksAndQueues;

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

    public void push(T data) {
        QueueNode<T> node = new QueueNode<>(data);
        if (isEmpty()) {
            this.head = this.tail = node;
        }
        else {
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
        Node<Integer> n4 = new Node<>(4);
        Node<Integer> n5 = new Node<>(5);
        n1.setLeft(n3);
        n1.setRight(n2);
        n2.setLeft(n5);
        n2.setRight(n4);

        Node<Integer> m1 = new Node<>(1);
        Node<Integer> m2 = new Node<>(2);
        Node<Integer> m3 = new Node<>(3);
        Node<Integer> m4 = new Node<>(4);
        Node<Integer> m5 = new Node<>(5);
        m1.setLeft(m2);
        m1.setRight(m3);
        m2.setLeft(m4);
        m2.setRight(m5);

        System.out.println(areAnagrams(n1, m1));

        // Example 2
        Node<Integer> one = new Node<>(1);
        Node<Integer> two = new Node<>(2);
        Node<Integer> three = new Node<>(3);
        Node<Integer> four = new Node<>(4);
        Node<Integer> five = new Node<>(5);
        one.setLeft(two);
        two.setLeft(five);
        one.setRight(three);
        two.setRight(four);

        Node<Integer> one1 = new Node<>(1);
        Node<Integer> two1 = new Node<>(2);
        Node<Integer> three1 = new Node<>(3);
        Node<Integer> four1 = new Node<>(4);
        Node<Integer> five1 = new Node<>(5);
        one1.setLeft(two1);
        two1.setLeft(five1);
        one1.setRight(four1);
        two1.setRight(three1);

        System.out.println(areAnagrams(one, one1));
    }

    private static <T> boolean areAnagrams(Node<T> root1, Node<T> root2) {
        Queue<Node<T>> queue1 = new Queue<>();
        Queue<Node<T>> queue2 = new Queue<>();

        queue1.push(root1);
        queue2.push(root2);

        while (!queue1.isEmpty() && !queue2.isEmpty()) {
            Node<T> node1 = queue1.pop();
            Node<T> node2 = queue2.pop();

            if (!node1.getData().equals(node2.getData())) {
                return false;
            }

            if (
                    (node1.getLeft() == null && node2.getRight() != null) ||
                    (node1.getLeft() != null && node2.getRight() == null) ||
                    (node1.getRight() == null && node2.getLeft() != null) ||
                    (node1.getRight() != null && node2.getLeft() == null)
            ) {
                return false;
            }

            if (node1.getLeft() != null && node2.getRight() != null) {
                queue1.push(node1.getLeft());
                queue2.push(node2.getRight());
            }
            if (node1.getRight() != null && node1.getLeft() != null) {
                queue1.push(node1.getRight());
                queue2.push(node2.getLeft());
            }
        }
        return true;
    }
}


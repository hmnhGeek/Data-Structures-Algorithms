package BinaryTrees.Problem2;


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


class Solution {
    public static void main(String[] args) {
        Queue<Integer> queue = new Queue<>();
        for (int i = 0; i < 6; i += 1) {
            queue.push(i);
        }
        while (!queue.isEmpty()) {
            System.out.println(queue.pop());
        }
    }
}
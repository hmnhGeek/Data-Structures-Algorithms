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
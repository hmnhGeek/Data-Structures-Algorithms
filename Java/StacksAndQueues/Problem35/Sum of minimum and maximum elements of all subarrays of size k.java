package StacksAndQueues.Problem35;


class Node<T> {
    private T data;
    private Node<T> prev;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }

    public Node<T> getPrev() {
        return prev;
    }

    public void setPrev(Node<T> prev) {
        this.prev = prev;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public T getData() {
        return data;
    }
}


class Deque<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public Deque() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void pushBack(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        }
        else {
            this.tail.setNext(node);
            node.setPrev(this.tail);
            this.tail = node;
        }
        this.length += 1;
    }

    public T popFront() {
        if (isEmpty()) {
            return null;
        }
        T item = this.head.getData();
        Node<T> nextHead = this.head.getNext();
        nextHead.setPrev(null);
        this.head.setNext(null);
        this.head = nextHead;
        this.length -= 1;
        return item;
    }
}
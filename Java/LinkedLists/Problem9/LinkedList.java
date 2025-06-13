package LinkedLists.Problem9;


class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }
}


public class LinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public LinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.setNext(node);
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T... args) {
        for (T x : args) {
            push(x);
        }
    }

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        if (this.length.equals(1)) return String.format("[%s]", this.head.getData());
        Node<T> curr = this.head;
        StringBuilder result = new StringBuilder("[");
        while (curr != this.tail) {
            result.append(String.format("%s, ", curr.getData()));
            curr = curr.getNext();
        }
        result.append(String.format("%s]", this.tail.getData()));
        return result.toString();
    }

    public void reverse() {
        Node<T> prev = null, curr = this.head;
        while (curr != null) {
            Node<T> nextOfCurr = curr.getNext();
            curr.setNext(prev);
            prev = curr;
            curr = nextOfCurr;
        }
        Node<T> t = this.tail;
        this.tail = this.head;
        this.head = t;
    }
}

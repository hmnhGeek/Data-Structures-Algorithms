package LinkedLists.Problem11;


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

    public Node<T> getHead() {
        return head;
    }

    public Node<T> getTail() {
        return tail;
    }

    public Integer getLength() {
        return length;
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

    public void build(T...args) {
        for (T x : args) {
            push(x);
        }
    }

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        if (this.length.equals(1)) return String.format("[%s]", this.head.getData());
        StringBuilder stringBuilder = new StringBuilder("[");
        Node<T> curr = this.head;
        while (curr != this.tail) {
            stringBuilder.append(String.format("%s, ", curr.getData()));
            curr = curr.getNext();
        }
        stringBuilder.append(String.format("%s]", this.tail.getData()));
        return stringBuilder.toString();
    }
}

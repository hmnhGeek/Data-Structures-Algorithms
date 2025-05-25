package LinkedLists.Problem8;

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

    public void setHead(Node<T> head) {
        this.head = head;
    }

    public void setTail(Node<T> tail) {
        this.tail = tail;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    private void push(T x) {
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
        for (T element : args) {
            push(element);
        }
    }

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        if (this.length.equals(1)) {
            return String.format("[%s]", this.head.getData());
        }
        Node<T> curr = this.head;
        StringBuilder result = new StringBuilder("[");
        while (curr != this.tail) {
            result.append(String.format("%s, ", curr.getData()));
            curr = curr.getNext();
        }
        result.append(String.format("%s]", this.tail.getData()));
        return result.toString();
    }
}

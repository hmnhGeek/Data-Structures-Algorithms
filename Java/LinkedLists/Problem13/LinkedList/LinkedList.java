package LinkedLists.Problem13.LinkedList;

public class LinkedList<T extends Comparable<T>> {
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

    public void setHead(Node<T> head) {
        this.head = head;
    }

    public Node<T> getTail() {
        return tail;
    }

    public void setTail(Node<T> tail) {
        this.tail = tail;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (this.length.equals(0)) {
            this.head = this.tail = node;
        } else {
            this.tail.setNext(node);
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T...args) {
        for (T i : args) {
            push(i);
        }
    }

    @Override
    public String toString() {
        if (this.length.equals(0)) return "[]";
        if (this.length.equals(1)) return String.format("[%s]", this.head.getData());
        Node<T> curr = this.head;
        StringBuilder result = new StringBuilder("[");
        while (curr != getTail()) {
            result.append(String.format("%s, ", curr.getData()));
            curr = curr.getNext();
        }
        result.append(String.format("%s]", getTail().getData()));
        return result.toString();
    }
}

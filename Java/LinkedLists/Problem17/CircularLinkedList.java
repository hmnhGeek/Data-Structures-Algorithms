package LinkedLists.Problem17;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class CircularLinkedList<T> {
    public Node<T> head;
    public Node<T> tail;

    public CircularLinkedList() {
        this.head = this.tail = null;
    }

    public boolean isEmpty() {
        return this.head == this.tail && this.head == null;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this.tail.next = this.head;
    }

    public void build(T...x) {
        for (T i : x) {
            push(i);
        }
    }

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        Node<T> curr = this.head;
        StringBuilder stringBuilder = new StringBuilder("[");
        while (curr != tail) {
            stringBuilder.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        stringBuilder.append(String.format("%s]", tail.data));
        return stringBuilder.toString();
    }
}

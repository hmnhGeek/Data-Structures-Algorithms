package LinkedLists.Problem32;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class LinkedList<T> {
    public Node<T> head, tail;
    public Integer length;

    public LinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (this.isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
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
        StringBuilder sb = new StringBuilder("[");
        Node<T> curr = this.head;
        while (curr != this.tail) {
            sb.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        sb.append(String.format("%s]", this.tail.data));
        return sb.toString();
    }

    public void reverse() {
        reverse(null, this.head);
        Node<T> prevHead = this.head;
        this.head = this.tail;
        this.tail = prevHead;
    }

    private void reverse(Node<T> prev, Node<T> curr) {
        if (curr == null) return;
        Node<T> nextCurr = curr.next;
        curr.next = prev;
        reverse(curr, nextCurr);
    }
}

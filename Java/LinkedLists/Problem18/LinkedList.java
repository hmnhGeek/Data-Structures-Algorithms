package LinkedLists.Problem18;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class LinkedList<T> {
    public Node<T> head;
    public Node<T> tail;
    public Integer length;

    public LinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (length == 0) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T...args) {
        for (T item : args) {
            push(item);
        }
    }

    @Override
    public String toString() {
        if (length == 0) return "[]";
        Node<T> curr = this.head;
        StringBuilder stringBuilder = new StringBuilder("[");
        while (curr != this.tail) {
            stringBuilder.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        stringBuilder.append(String.format("%s]", this.tail.data));
        return stringBuilder.toString();
    }

    public Node<T> getMiddleNode() {
        if (length == 0) return null;
        Node<T> slow = this.head;
        Node<T> fast = this.head.next;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}

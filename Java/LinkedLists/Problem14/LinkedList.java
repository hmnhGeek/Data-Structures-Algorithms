package LinkedLists.Problem14;


class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class LinkedList<T extends Comparable<T>> {
    public Node<T> head;
    public Node<T> tail;
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
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T...args) {
        for (T arg : args) {
            push(arg);
        }
    }

    @Override
    public String toString() {
        if (this.length == 0) return "[]";
        StringBuilder result = new StringBuilder("[");
        Node<T> curr = this.head;
        while (curr != this.tail) {
            result.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        result.append(String.format("%s]", this.tail.data));
        return result.toString();
    }
}

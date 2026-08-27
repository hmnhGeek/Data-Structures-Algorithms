package LinkedLists.Problem30;


class Node<T> {
    public T data;
    public Node<T> next, random;

    public Node(T data) {
        this.data = data;
        this.next = this.random = null;
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
        if (isEmpty()) {
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
        StringBuilder result = new StringBuilder("[");
        Node<T> curr = this.head;
        while (curr != this.tail) {
            result.append(String.format("(%s, %s), ", curr.data, curr.random != null ? curr.random.data : null));
            curr = curr.next;
        }
        result.append(String.format("(%s, %s)]", curr.data, curr.random != null ? curr.random.data : null));
        return result.toString();
    }
}

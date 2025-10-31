package LinkedLists.Problem16;


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
    public int length;

    public LinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (this.length == 0) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T...x) {
        for (T i : x) {
            this.push(i);
        }
    }

    @Override
    public String toString() {
        if (this.length == 0) return "[]";
        Node<T> curr = this.head;
        StringBuilder result = new StringBuilder("[");
        while (curr != this.tail) {
            result.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        result.append(String.format("%s]", this.tail.data));
        return result.toString();
    }
}

package LinkedLists.Problem23;


class Node<T extends Comparable<T>> implements Comparable<Node<T>> {
    public T data;
    public Node<T> prev, next;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }

    @Override
    public int compareTo(Node<T> o) {
        return this.data.compareTo(o.data);
    }
}


public class DoublyLinkedList<T extends Comparable<T>> {
    public Node<T> head, tail;
    public Integer length;

    public DoublyLinkedList() {
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
            node.prev = this.tail;
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

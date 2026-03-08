package LinkedLists.Problem21;


class Node<T> {
    public T data;
    public Node<T> prev, next;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }
}


public class DoublyLinkedList<T> {
    public Node<T> head, tail;

    public DoublyLinkedList() {
        this.head = this.tail = null;
    }

    private void push(T x) {
        Node<T> node = new Node<>(x);
        if (this.head == null) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
    }

    public void build(T...args) {
        for (T x : args) {
            push(x);
        }
    }
}

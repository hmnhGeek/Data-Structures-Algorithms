package LinkedLists.Problem20;


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
    public Integer length;

    public DoublyLinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (length == 0) {
            head = tail = node;
        } else {
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        length += 1;
    }

    public void build(T...args) {
        for (T x : args) {
            push(x);
        }
    }

    @Override
    public String toString() {
        if (length == 0) return "[]";
        Node<T> curr = head;
        StringBuilder result = new StringBuilder("[");
        while (curr != tail) {
            result.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        result.append(String.format("%s]", tail.data));
        return result.toString();
    }
}

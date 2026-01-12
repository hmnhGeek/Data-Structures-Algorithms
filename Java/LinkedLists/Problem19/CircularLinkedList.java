package LinkedLists.Problem19;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class CircularLinkedList<T> {
    public Node<T> head, tail;
    public Integer length;

    public CircularLinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            head = tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
        tail.next = head;
        length += 1;
    }

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        Node<T> curr = head;
        StringBuilder sb = new StringBuilder("[");
        while (curr != tail) {
            sb.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        sb.append(String.format("%s]", tail.data));
        return sb.toString();
    }
}

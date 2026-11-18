package PracticeSet1.Heap.Problem10.LinkedList;

public class LinkedList<T> {
    public Node<T> head, tail;
    public Integer length;

    @SafeVarargs
    public LinkedList(T...args) {
        this.head = this.tail = null;
        this.length = 0;
        for (T x : args) {
            push(x);
        }
    }

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

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        Node<T> curr = this.head;
        StringBuilder sb = new StringBuilder("[");
        while (curr != this.tail) {
            sb.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        sb.append(String.format("%s]", this.tail.data));
        return sb.toString();
    }
}

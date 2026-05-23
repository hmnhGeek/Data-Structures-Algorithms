package LinkedLists.Problem24;

public class DoublyLinkedList<T> {
    public Node<T> head, tail;

    public DoublyLinkedList() {
        this.head = this.tail = null;
    }

    public boolean isEmpty() {
        return this.head == null;
    }

    public void insert(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
    }

    public void build(T...args) {
        for (T x : args) {
            insert(x);
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
}

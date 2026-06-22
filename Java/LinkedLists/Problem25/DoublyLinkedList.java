package LinkedLists.Problem25;

public class DoublyLinkedList<T> {
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
            this.tail.next = node;
            node.prev = this.tail;
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
        StringBuilder sb = new StringBuilder("[");
        while (curr != this.tail) {
            sb.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        sb.append(String.format("%s]", this.tail.data));
        return sb.toString();
    }

    public void reverse() {
        if (isEmpty()) return;
        Node<T> prev = null, curr = this.head;
        while (curr != null) {
            Node<T> nextCurr = curr.next;
            curr.next = prev;
            curr.prev = nextCurr;
            prev = curr;
            curr = nextCurr;
        }
        Node<T> currHead = this.head;
        this.head = this.tail;
        this.tail = currHead;
    }
}

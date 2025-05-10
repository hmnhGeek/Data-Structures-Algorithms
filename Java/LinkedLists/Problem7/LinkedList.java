package LinkedLists.Problem7;

import java.util.HashSet;
import java.util.Set;

public class LinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public LinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (this.length.equals(0)) {
            this.head = this.tail = node;
        } else {
            this.tail.setNext(node);
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T... args) {
        for (T x : args) {
            this.push(x);
        }
    }

    @Override
    public String toString() {
        if (this.length == 0) return "[]";
        if (this.length == 1) return String.format("[%s]", this.head.getData());
        StringBuilder stringBuilder = new StringBuilder(String.format("[%s, ", this.head.getData()));
        Node<T> curr = this.head.getNext();
        while (curr != this.tail) {
            stringBuilder.append(String.format("%s, ", curr.getData()));
            curr = curr.getNext();
        }
        stringBuilder.append(String.format("%s]", this.tail.getData()));
        return stringBuilder.toString();
    }

    public void removeDuplicates() {
        if (this.length == 0 || this.length == 1) return;
        Set<T> set = new HashSet<>();
        Node<T> curr = this.head;
        Node<T> dummyNode = new Node<>(null);
        Node<T> prev = dummyNode;
        while (curr != null) {
            Node<T> nextCurr = curr.getNext();

            if (!set.contains(curr.getData())) {
                prev.setNext(curr);
                prev = curr;
                set.add(curr.getData());
                curr.setNext(null);
            } else  {
                this.length -= 1;
            }
            curr = nextCurr;
        }
        this.head = dummyNode.getNext();
        Node<T> node = this.head;
        while (node.getNext() != null) {
            node = node.getNext();
        }
        this.tail = node;
    }
}

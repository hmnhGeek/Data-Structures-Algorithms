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
        // edge cases
        if (this.length == 0 || this.length == 1) return;

        // create a hash set to store visited data nodes.
        Set<T> set = new HashSet<>();

        // important pointers
        Node<T> curr = this.head;
        Node<T> dummyNode = new Node<>(null);
        Node<T> prev = dummyNode;

        // traverse the linked list in O(n) time.
        while (curr != null) {
            // store the pointer to the next curr node.
            Node<T> nextCurr = curr.getNext();

            // if the current data point is first visited
            if (!set.contains(curr.getData())) {
                // link it with prev node
                prev.setNext(curr);
                prev = curr;

                // add this data point into the set
                set.add(curr.getData());

                // de-link curr from the original list.
                curr.setNext(null);
            } else  {
                // since the data point is already present in the set, we are not adding it,
                // simply reduce the length.
                this.length -= 1;
            }

            // move to the next curr.
            curr = nextCurr;
        }

        // update head and tail pointers.
        this.head = dummyNode.getNext();
        this.tail = prev;
    }
}

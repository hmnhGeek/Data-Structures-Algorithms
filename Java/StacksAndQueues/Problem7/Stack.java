package StacksAndQueues.Problem7;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class Stack<T> {
    public Node<T> head;
    public Node<T> tail;
    public Integer length;

    public Stack() {
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
            node.next = this.head;
            this.head = node;
        }
        this.length += 1;
    }

    public T pop() {
        if (isEmpty()) return null;
        T item = this.head.data;
        this.head = this.head.next;
        this.length -= 1;
        return item;
    }

    public void reverse() {
        Node<T> prev = null, curr = this.head;
        while (curr != null) {
            Node<T> nextCurr = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextCurr;
        }
        Node<T> orgHead = this.head, orgTail = this.tail;
        this.head = orgTail;
        this.tail = orgHead;
    }

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        Node<T> curr = this.head;
        StringBuilder stringBuilder = new StringBuilder("]");
        while (curr != this.tail) {
            stringBuilder.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        stringBuilder.append(String.format("%s[", this.tail.data));
        stringBuilder.reverse();
        return stringBuilder.toString();
    }
}

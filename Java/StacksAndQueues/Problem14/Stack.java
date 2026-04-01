package StacksAndQueues.Problem14;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class Stack<T> {
    public Node<T> head, tail;
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
        reverseStack(null, this.head);
        Node<T> temp = this.head;
        this.head = this.tail;
        this.tail = temp;
    }

    private void reverseStack(Node<T> prev, Node<T> curr) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        if (curr == null) {
            return;
        }
        Node<T> nextCurr = curr.next;
        curr.next = prev;
        reverseStack(curr, nextCurr);
    }

    @Override
    public String toString() {
        if (this.length == 0) return "[]";
        StringBuilder sb = new StringBuilder("[");
        Node<T> curr = this.head;
        while (curr.next != null) {
            sb.append(String.format("%s, ", curr.data));
            curr = curr.next;
        }
        sb.append(String.format("%s]", this.tail.data));
        return sb.toString();
    }
}

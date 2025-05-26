package StacksAndQueues.Problem37;

class Node<T> {
    private T data;
    private Node<T> next;
    private Node<T> prev;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public Node<T> getPrev() {
        return prev;
    }

    public void setPrev(Node<T> prev) {
        this.prev = prev;
    }
}


public class DoublyLinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public DoublyLinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public Node<T> push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.setNext(node);
            node.setPrev(this.tail);
            this.tail = node;
        }
        this.length += 1;
        return node;
    }

    public void deleteNode(Node<T> node) {
        Node<T> prevNode = node.getPrev();
        Node<T> nextNode = node.getNext();

        if (prevNode == null) {
            nextNode.setPrev(null);
            this.head = nextNode;
        } else if (nextNode == null) {
            prevNode.setNext(null);
            this.tail = prevNode;
        } else {
            prevNode.setNext(nextNode);
            nextNode.setPrev(prevNode);
        }

        this.length -= 1;
    }
}

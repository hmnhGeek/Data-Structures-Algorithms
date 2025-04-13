package LinkedLists.Problem5;


import java.util.Arrays;

class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public T getData() {
        return data;
    }
}

class LinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public LinkedList() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public Node<T> getHead() {
        return head;
    }

    public Node<T> getTail() {
        return tail;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        }
        else {
            this.tail.setNext(node);
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T... args) {
        Arrays.stream(args).toList().forEach(this::push);
    }
}


class Solution {
    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> linkedList1 = new LinkedList<>();
        linkedList1.build(1, 3, 2, 4, 5);
        System.out.println(getLoopStartNode(linkedList1));
        linkedList1.getTail().setNext(linkedList1.getHead().getNext());
        System.out.println(getLoopStartNode(linkedList1).getData());
    }

    public static <T> Node<T> getLoopStartNode(LinkedList<T> linkedList) {
        Node<T> slow = linkedList.getHead(), fast = linkedList.getHead();
        while (slow != null && fast != null && fast.getNext() != null) {
            slow = slow.getNext();
            fast = fast.getNext().getNext();
            if (slow == fast) {
                slow = linkedList.getHead();
                while (slow != fast) {
                    slow = slow.getNext();
                    fast = fast.getNext();
                }
                return slow;
            }
        }
        return null;
    }
}
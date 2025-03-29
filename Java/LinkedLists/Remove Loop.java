package LinkedLists;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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

    public Node<T> getHead() {
        return head;
    }

    public void setHead(Node<T> head) {
        this.head = head;
    }

    public Node<T> getTail() {
        return tail;
    }

    public void setTail(Node<T> tail) {
        this.tail = tail;
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
            setHead(node);
            setTail(node);
        }
        else {
            tail.setNext(node);
            setTail(node);
        }
        length += 1;
    }

    @Override
    public String toString() {
        if (isEmpty()) {
            return "[]";
        }
        StringBuilder result = new StringBuilder(String.format("[%s", getHead().getData()));
        Node<T> curr = getHead().getNext();
        while (curr != getTail()) {
            result.append(String.format(", %s", curr.getData()));
            curr = curr.getNext();
        }
        result.append(String.format(", %s]", getTail().getData()));
        return result.toString();
    }

    public boolean hasLoop() {
        Node<T> slow = getHead();
        Node<T> fast = getHead();
        while (slow != null && fast != null && fast.getNext() != null) {
            slow = slow.getNext();
            fast = fast.getNext().getNext();
            if(slow == fast) {
                return true;
            }
        }
        return false;
    }

    public void removeLoop() {
        if (hasLoop()) {
            getTail().setNext(null);
        }
    }
}

class Solution {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 10, -19);
        LinkedList<Integer> linkedList = new LinkedList<>();
        list.forEach(linkedList::push);
        System.out.println(linkedList);
        System.out.println(linkedList.hasLoop());
        linkedList.getTail().setNext(linkedList.getHead().getNext().getNext());
        System.out.println(linkedList.hasLoop());
        linkedList.removeLoop();
        System.out.println(linkedList.hasLoop());
    }
}
package LinkedLists.Problem6;

class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public T getData() {
        return data;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
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

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.setNext(node);
            this.tail = node;
        }
        this.length += 1;
    }

    public void build(T... args) {
        for (T arg : args) {
            push(arg);
        }
    }

    @Override
    public String toString() {
        if (this.length.equals(0)) {
            return "[]";
        }
        if (this.length.equals(1)) {
            return "[" + this.head.getData() + "]";
        }
        StringBuilder result = new StringBuilder("[" + this.head.getData() + ", ");
        Node<T> curr = this.head.getNext();
        while (curr != this.tail) {
            result.append(curr.getData()).append(", ");
            curr = curr.getNext();
        }
        result.append(this.tail.getData()).append("]");
        return result.toString();
    }

    public void removeDuplicates() {
        Node<T> curr = this.head;
        Node<T> temp = this.head;
        while (curr != null) {
            while (curr.getData().equals(temp.getData())) {
                temp = temp.getNext();
                if (temp == null) {
                    this.tail = curr;
                    break;
                }
            }
            curr.setNext(temp);
            curr = temp;
        }
    }
}


class Solution {
    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(2, 2, 2, 4, 6, 6);
        System.out.println(l1);
        l1.removeDuplicates();
        System.out.println(l1);
    }
}
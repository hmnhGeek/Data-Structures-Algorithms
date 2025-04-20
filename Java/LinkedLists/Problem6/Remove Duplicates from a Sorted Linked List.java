// Problem link - https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1


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
        /*
            Time complexity is O(n) and space complexity is O(1).
         */

        // make two pointers, initially pointing to head of the linked list.
        Node<T> curr = this.head;
        Node<T> temp = this.head;

        // traverse the linked list
        while (curr != null) {
            // if the curr and temp nodes have same data, move temp to next.
            while (curr.getData().equals(temp.getData())) {
                // also, if curr and temp are different nodes, reduce the length of the linked list.
                if (curr != temp) length -= 1;
                temp = temp.getNext();

                // if temp reaches null, then it means curr would be the last node and no further iteration is needed.
                if (temp == null) {
                    this.tail = curr;
                    break;
                }
            }

            // update curr.next and move curr to temp.
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

        // Example 2
        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(2, 2, 2, 2);
        System.out.println(l2);
        l2.removeDuplicates();
        System.out.println(l2);

        // Example 3
        LinkedList<Integer> l3 = new LinkedList<>();
        l3.build(1, 6, 7, 9, 0, 0, 0, 0);
        System.out.println(l3);
        l3.removeDuplicates();
        System.out.println(l3);
    }
}
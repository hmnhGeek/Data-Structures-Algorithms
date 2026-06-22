package LinkedLists.Problem25;

import java.util.List;

public class Solution {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> db = new DoublyLinkedList<>();
        db.build(1, 2, 3, 4, 5, 6);
        System.out.println(db);
        reverseInParts(db, 4);
        System.out.println(db);
    }

    public static <T> void reverseInParts(DoublyLinkedList<T> dll, int k) {
        Node<T> curr = dll.head;
        Node<T> prev = null;
        while (curr != null) {
            Node<T> temp = curr;
            Node<T> prevOfTemp = temp.prev;
            int counter = 1;
            int length = 0;
            while (counter != k && temp != null) {
                prevOfTemp = temp;
                temp = temp.next;
                counter += 1;
                length += 1;
            }
            if (temp == null) {
                temp = prevOfTemp;
            }
            Node<T> nextCurr = temp.next;
            if (temp != null) {
                temp.next = null;
            }
            if (nextCurr != null) {
                nextCurr.prev = null;
            }
            DoublyLinkedList<T> sublist = new DoublyLinkedList<>();
            sublist.head = curr;
            sublist.tail = temp;
            sublist.length = length;
            List<Node<T>> pointers = sublist.reverse();
            pointers.getLast().next = nextCurr;
            if (nextCurr != null) {
                nextCurr.prev = pointers.getLast();
            } else {
                dll.tail = pointers.getLast();
            }
            if (prev == null) {
                dll.head = pointers.getFirst();
            } else {
                prev.next = pointers.getFirst();
            }
            prev = curr;
            curr = nextCurr;
        }
    }
}

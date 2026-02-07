// Problem link - https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1


package LinkedLists.Problem20;

public class Solution {
    public static void main(String[] args) {
        test(1, 2, 2, 3, 4, -1);
        test(3, 4, 5);
        test(75, 122, 59, 196);
    }

    private static <T> void test(T...args) {
        DoublyLinkedList<T> dll = new DoublyLinkedList<>();
        dll.build(args);
        reverseDll(dll);
        System.out.println(dll);
    }

    public static <T> void reverseDll(DoublyLinkedList<T> doublyLinkedList) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        Node<T> prev = null, curr = doublyLinkedList.head;
        while (curr != null) {
            Node<T> nextCurr = curr.next;
            curr.next = prev;
            curr.prev = nextCurr;
            prev = curr;
            curr = nextCurr;
        }
        Node<T> origTail = doublyLinkedList.tail;
        doublyLinkedList.tail = doublyLinkedList.head;
        doublyLinkedList.head = origTail;
    }
}

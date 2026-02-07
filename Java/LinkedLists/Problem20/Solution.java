package LinkedLists.Problem20;

public class Solution {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.build(1, 2, 2, 3, 4, -1);
        reverseDll(dll);
        System.out.println(dll);
    }

    public static <T> void reverseDll(DoublyLinkedList<T> doublyLinkedList) {
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

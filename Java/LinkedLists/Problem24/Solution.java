// Problem link - https://www.geeksforgeeks.org/dsa/rotate-doubly-linked-list-n-nodes/


package LinkedLists.Problem24;

public class Solution {
    public static void main(String[] args) {
        rotate(2, 1, 2, 3, 4, 5);
        rotate(3, 2, 6, 5, 4);
        rotate(2, 1, 2, 3, 4, 5, 6);
        rotate(3, 3, 4, 5, 1);
        rotate(2, 1, 2, 3, 1);
    }

    public static void rotate(Integer p, Integer...args) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.build(args);
        System.out.println(dll);
        int counter = 0;
        Node<Integer> trackerNode = dll.head;
        while (counter != p) {
            trackerNode = trackerNode.next;
            counter += 1;
        }
        Node<Integer> temp = dll.tail;
        Node<Integer> curr = dll.head;
        while (curr != trackerNode) {
            Node<Integer> nextCurr = curr.next;
            temp.next = curr;
            curr.prev = temp;
            temp = curr;
            curr = nextCurr;
        }
        dll.head = trackerNode;
        dll.tail = temp;
        System.out.println(dll);
        System.out.println();
    }
}

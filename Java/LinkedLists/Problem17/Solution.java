// Problem link - https://www.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1


package LinkedLists.Problem17;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    private static <T> Node<T> findMiddleNode(CircularLinkedList<T> circularLinkedList) {
        if (circularLinkedList.isEmpty()) return null;
        circularLinkedList.tail.next = null;
        Node<T> slow = circularLinkedList.head;
        Node<T> fast = circularLinkedList.head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        circularLinkedList.tail.next = circularLinkedList.head;
        return slow;
    }

    public static <T> List<CircularLinkedList<T>> split(CircularLinkedList<T> circularLinkedList) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        if (circularLinkedList.isEmpty()) return new ArrayList<>();
        if (circularLinkedList.head == circularLinkedList.tail) return List.of(circularLinkedList, null);

        CircularLinkedList<T> secondList = new CircularLinkedList<>();
        Node<T> middleNode = findMiddleNode(circularLinkedList);

        circularLinkedList.tail.next = null;
        Node<T> nextNode = middleNode.next;
        middleNode.next = circularLinkedList.head;
        Node<T> toBeTailOfSecondList = circularLinkedList.tail;
        circularLinkedList.tail = middleNode;
        toBeTailOfSecondList.next = nextNode;
        secondList.head = nextNode;
        secondList.tail = toBeTailOfSecondList;
        return List.of(circularLinkedList, secondList);
    }

    public static void main(String[] args) {
        CircularLinkedList<Integer> circularLinkedList = new CircularLinkedList<>();
        circularLinkedList.build(1, 2, 3, 4, 4, 5);
        System.out.println(split(circularLinkedList));

        CircularLinkedList<Integer> circularLinkedList1 = new CircularLinkedList<>();
        circularLinkedList1.build(10, 4, 9);
        System.out.println(split(circularLinkedList1));

        CircularLinkedList<Integer> circularLinkedList2 = new CircularLinkedList<>();
        circularLinkedList2.build(10, 4, 9, 10);
        System.out.println(split(circularLinkedList2));
    }
}

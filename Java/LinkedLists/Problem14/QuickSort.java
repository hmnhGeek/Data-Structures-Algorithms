package LinkedLists.Problem14;

import java.util.Arrays;
import java.util.List;

public class QuickSort {

    // Partition the list around pivot; return head and tail for left and right sublists
    private static <T extends Comparable<T>> List<Node<T>> partition(Node<T> head) {
        T pivotVal = head.data;
        Node<T> current = head.next;
        head.next = null; // detach pivot

        Node<T> leftHead = null, leftTail = null;
        Node<T> rightHead = null, rightTail = null;

        while (current != null) {
            Node<T> nextNode = current.next;
            current.next = null;
            if (current.data.compareTo(pivotVal) <= 0) {
                if (leftHead == null) {
                    leftHead = leftTail = current;
                } else {
                    leftTail.next = current;
                    leftTail = current;
                }
            } else {
                if (rightHead == null) {
                    rightHead = rightTail = current;
                } else {
                    rightTail.next = current;
                    rightTail = current;
                }
            }
            current = nextNode;
        }
        return Arrays.asList(leftHead, leftTail, rightHead, rightTail, head);
    }

    public static <T extends Comparable<T>> LinkedList<T> sort(LinkedList<T> list) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        if (list.head == null || list.head.next == null) {
            return list; // already sorted
        }

        // Partition list around pivot (first node)
        List<Node<T>> parts = partition(list.head);
        Node<T> leftHead = parts.get(0);
        Node<T> leftTail = parts.get(1);
        Node<T> rightHead = parts.get(2);
        Node<T> rightTail = parts.get(3);
        Node<T> pivot = parts.get(4);

        // Create sublists for left and right
        LinkedList<T> leftList = new LinkedList<>();
        LinkedList<T> rightList = new LinkedList<>();

        leftList.head = leftHead;
        leftList.tail = leftTail;
        rightList.head = rightHead;
        rightList.tail = rightTail;

        // Recursively sort left list
        if (leftList.head != null) {
            leftList = sort(leftList);
        }

        // Recursively sort right list
        if (rightList.head != null) {
            rightList = sort(rightList);
        }

        // Connect left list -> pivot -> right list
        // Address edge cases:
        // 1. Left list empty, so pivot is the start
        // 2. Left list exists, connect tail to pivot
        // 3. Pivot's next to right list's head
        if (leftList.head != null) {
            leftList.tail.next = pivot;
            list.head = leftList.head;
        } else {
            list.head = pivot; // pivot is the start
        }

        // Connect pivot to right list
        pivot.next = rightList.head;

        // Update list tail
        if (rightList.tail != null) {
            list.tail = rightList.tail;
        } else {
            list.tail = pivot;
        }

        return list;
    }
}


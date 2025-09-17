package LinkedLists.Problem14;

import java.util.Arrays;
import java.util.List;

public class QuickSort {
    public static <T extends Comparable<T>> List<Node<T>> findPartition(Node<T> pivot, Node<T> left, Node<T> right) {
        Node<T> temp = pivot.next;
        while (temp != null) {
            Node<T> nextOfTemp = temp.next;
            if (temp.data.compareTo(pivot.data) <= 0) {
                temp.next = left;
                left = temp;
            } else {
                temp.next = right;
                right = temp;
            }
            temp = nextOfTemp;
        }
        return Arrays.asList(left, right);
    }

    public static <T extends Comparable<T>> LinkedList<T> sort(LinkedList<T> linkedList) {
        if (linkedList.head == linkedList.tail) {
            return linkedList;
        }
        Node<T> originalHead = linkedList.head;
        Node<T> left = null, right = null;
        List<Node<T>> partitionedResult = findPartition(linkedList.head, left, right);
        left = partitionedResult.getFirst();
        right = partitionedResult.getLast();
        LinkedList<T> leftLinkedList = new LinkedList<>(), rightLinkedList = new LinkedList<>();
        leftLinkedList.head = left;
        rightLinkedList.head = right;

        Node<T> leftHead = left;
        Integer leftListLength = 1;
        while (leftHead != null && leftHead.next != null) {
            leftListLength += 1;
            leftHead = leftHead.next;
        }
        if (leftHead != null) {
            leftLinkedList.length = leftListLength;
            leftLinkedList.tail = leftHead;
        }

        Node<T> rightHead = right;
        Integer rightListLength = 1;
        while (rightHead != null && rightHead.next != null) {
            rightListLength += 1;
            rightHead = rightHead.next;
        }
        if (rightHead != null) {
            rightLinkedList.length = rightListLength;
            rightLinkedList.tail = rightHead;
        }

        leftLinkedList = sort(leftLinkedList);
        rightLinkedList = sort(rightLinkedList);
        if (!leftLinkedList.isEmpty()) {
            leftLinkedList.tail.next = linkedList.head;
            linkedList.head.next = rightLinkedList.head;
            linkedList.head = leftLinkedList.head;
        }
        if (!rightLinkedList.isEmpty()) {
            linkedList.tail = rightLinkedList.tail;
        } else {
            linkedList.tail = originalHead;
        }
        return linkedList;
    }
}

package LinkedLists.Problem14;

import java.util.Arrays;
import java.util.List;

public class QuickSort {
    public static <T extends Comparable<T>> List<Node<T>> findPartition(Node<T> pivot, Node<T> left, Node<T> right) {
        // point the temp to the next node of pivot.
        Node<T> temp = pivot.next;

        // loop the temp until it becomes null (temp is next to pivot at start).
        while (temp != null) {
            // store the next of temp so that we don't lose the sequence.
            Node<T> nextOfTemp = temp.next;

            // if temp's data <= pivot's data, push temp node to left partition.
            if (temp.data.compareTo(pivot.data) <= 0) {
                temp.next = left;
                left = temp;
            } else {
                // else push to right partition.
                temp.next = right;
                right = temp;
            }

            // update temp
            temp = nextOfTemp;
        }

        // return the starting points of left and right partitions.
        return Arrays.asList(left, right);
    }

    public static <T extends Comparable<T>> LinkedList<T> sort(LinkedList<T> linkedList) {
        // if there is a single element in the list, or none, then we can return the list as is because it is already sorted.
        if (linkedList.head == linkedList.tail) {
            return linkedList;
        }

        // store the current head for later use.
        Node<T> originalHead = linkedList.head;

        // store left and right nodes for keeping the heads of the left partition and right partition lists.
        Node<T> left = null, right = null;

        // get the heads of the partitioned lists.
        List<Node<T>> partitionedResult = findPartition(linkedList.head, left, right);
        left = partitionedResult.getFirst();
        right = partitionedResult.getLast();

        // construct the left partition list and right partition list.
        LinkedList<T> leftLinkedList = new LinkedList<>(), rightLinkedList = new LinkedList<>();
        leftLinkedList.head = left;
        rightLinkedList.head = right;

        // update the tail of the left partition.
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

        // update the tail of the right partition.
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

        // sort the left and right partitions now.
        leftLinkedList = sort(leftLinkedList);
        rightLinkedList = sort(rightLinkedList);

        // Now the left and right partitions are sorted and the current head node is at its correct position.
        // So, we just need to wire the nodes correctly now to get the complete sorted list.

        // if left partition is present
        if (!leftLinkedList.isEmpty()) {
            // connect the left partition's tail to the head node of the list.
            leftLinkedList.tail.next = linkedList.head;

            // wire the head node of the list to the right partition's head.
            linkedList.head.next = rightLinkedList.head;

            // update the head of the original list to the left partition's head.
            linkedList.head = leftLinkedList.head;
        }

        // note that if the left partition is empty, the original head is the correct head already.

        // if the right partition is not empty
        if (!rightLinkedList.isEmpty()) {
            // update the tail of the list to right partition's tail
            linkedList.tail = rightLinkedList.tail;
        } else {
            // otherwise, the tail of the original list will be same as original head.
            linkedList.tail = originalHead;
        }

        // return the completed sorted list
        return linkedList;
    }
}

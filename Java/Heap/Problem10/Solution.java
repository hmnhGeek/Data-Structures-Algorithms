// Problem link - https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1


package Heap.Problem10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> l1 = getLinkedList(1, 3, 7);
        LinkedList<Integer> l2 = getLinkedList(2, 4, 8);
        LinkedList<Integer> l3 = getLinkedList(9);
        System.out.println(mergeSortedLinkedLists(Arrays.asList(l1, l2, l3)));

        // Example 2
        LinkedList<Integer> l4 = getLinkedList(1, 3);
        LinkedList<Integer> l5 = getLinkedList(8);
        LinkedList<Integer> l6 = getLinkedList(4, 5, 6);
        System.out.println(mergeSortedLinkedLists(Arrays.asList(l4, l5, l6)));
    }

    private static <T extends Comparable<T>> LinkedList<T> getLinkedList(T...args) {
        LinkedList<T> l = new LinkedList<>();
        l.build(args);
        return l;
    }

    public static <T extends Comparable<T>> LinkedList<T> mergeSortedLinkedLists(List<LinkedList<T>> linkedListLists) {
        /*
            Time complexity is O(nk * log(k)) and space complexity is O(k).
         */

        MinHeap<Node<T>> minHeap = new MinHeap<>();
        Integer finalLength = 0;

        // This will take O(k * log(k)) time and O(k) space.
        for (LinkedList<T> linkedList : linkedListLists) {
            finalLength += linkedList.getLength();
            minHeap.insert(linkedList.getHead());
        }

        // This will take O(k * n * log(k)) time assuming n is the avg length of each list.
        Node<T> dummyNode = new Node<>(null);
        Node<T> temp = dummyNode;
        while (!minHeap.isEmpty()) {
            Node<T> node = minHeap.pop();
            temp.setNext(node);
            temp = node;
            if (node.getNext() != null) {
                minHeap.insert(node.getNext());
            }
        }
        LinkedList<T> result = new LinkedList<>();
        result.setHead(dummyNode.getNext());
        result.setTail(temp);
        result.setLength(finalLength);
        return result;
    }
}

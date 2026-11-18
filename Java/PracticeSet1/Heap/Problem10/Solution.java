package PracticeSet1.Heap.Problem10;

import PracticeSet1.Heap.Problem10.Heap.impl.MinHeap;
import PracticeSet1.Heap.Problem10.LinkedList.LinkedList;
import PracticeSet1.Heap.Problem10.LinkedList.Node;
import PracticeSet1.Heap.Problem10.Misc.Element;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> l1 = new LinkedList<>(1, 3, 7);
        LinkedList<Integer> l2 = new LinkedList<>(2, 4, 8);
        LinkedList<Integer> l3 = new LinkedList<>(9);
        LinkedList<LinkedList<Integer>> lists = new LinkedList<>(l1, l2, l3);
        LinkedList<Integer> mergedList = mergeKSortedLinkedLists(lists);
        System.out.println(mergedList);
    }

    public static <T extends Comparable<T>> LinkedList<T> mergeKSortedLinkedLists(LinkedList<LinkedList<T>> linkedLists) {
        if (linkedLists.isEmpty()) return null;
        MinHeap<Element<T>> pq = initializeMinHeap(linkedLists);
        Node<T> dummyNode = new Node<>(null);
        Node<T> temp = dummyNode;
        Integer mergedLinkedListLength = 0;
        LinkedList<T> mergedLinkedList = new LinkedList<>();
        while (!pq.isEmpty()) {
            Node<T> node = pq.pop().node;
            Node<T> nextNode = node.next;
            temp.next = node;
            temp = node;
            node.next = null;
            if (nextNode != null) {
                pq.insert(new Element<>(nextNode));
            }
            mergedLinkedListLength += 1;
        }
        mergedLinkedList.head = dummyNode.next;
        mergedLinkedList.tail = temp;
        mergedLinkedList.length = mergedLinkedListLength;
        return mergedLinkedList;
    }

    private static <T extends Comparable<T>> MinHeap<Element<T>> initializeMinHeap(LinkedList<LinkedList<T>> linkedLists) {
        MinHeap<Element<T>> pq = new MinHeap<>();
        Node<LinkedList<T>> curr = linkedLists.head;
        while (curr != null) {
            pq.insert(new Element<>(curr.data.head));
            curr = curr.next;
        }
        return pq;
    }
}

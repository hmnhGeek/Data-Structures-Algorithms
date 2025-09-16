package Heap.Problem10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = getLinkedList(1, 3, 7);
        LinkedList<Integer> l2 = getLinkedList(2, 4, 8);
        LinkedList<Integer> l3 = getLinkedList(9);
        System.out.println(mergeSortedLinkedLists(Arrays.asList(l1, l2, l3)));
    }

    private static <T extends Comparable<T>> LinkedList<T> getLinkedList(T...args) {
        LinkedList<T> l = new LinkedList<>();
        l.build(args);
        return l;
    }

    public static <T extends Comparable<T>> LinkedList<T> mergeSortedLinkedLists(List<LinkedList<T>> linkedListLists) {
        MinHeap<Node<T>> minHeap = new MinHeap<>();
        Integer finalLength = 0;
        for (LinkedList<T> linkedList : linkedListLists) {
            finalLength += linkedList.getLength();
            minHeap.insert(linkedList.getHead());
        }
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

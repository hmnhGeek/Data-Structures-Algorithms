package LinkedLists.Problem31;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(1, 3, 7);
        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(2, 4, 8);
        LinkedList<Integer> l3 = new LinkedList<>();
        l3.build(9);
        LinkedList<Integer> merged1 = mergeSortedLinkedLists(Arrays.asList(l1, l2, l3));
        System.out.println(merged1);
    }

    public static <T extends Comparable<T>> LinkedList<T> mergeSortedLinkedLists(List<LinkedList<T>> linkedLists) {
        MinHeap<Node<T>> minHeap = new MinHeap<>();
        for (LinkedList<T> linkedList : linkedLists) {
            minHeap.insert(linkedList.head);
        }
        Node<T> dummyNode = new Node<>(null);
        Node<T> temp = dummyNode;
        Integer length = 0;
        while (!minHeap.isEmpty()) {
            Node<T> curr = minHeap.pop();
            length += 1;
            Node<T> nextCurr = curr.next;
            temp.next = curr;
            temp = curr;
            curr.next = null;
            if (nextCurr != null) {
                minHeap.insert(nextCurr);
            }
        }
        LinkedList<T> resultant = new LinkedList<>();
        resultant.head = dummyNode.next;
        resultant.tail = temp;
        resultant.length = length;
        return resultant;
    }
}

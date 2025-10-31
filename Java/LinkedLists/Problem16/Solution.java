// Problem link - https://www.geeksforgeeks.org/problems/circular-linked-list/1


package LinkedLists.Problem16;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> linkedList1 = new LinkedList<>();
        linkedList1.build(2, 4, 6, 7, 5);
        linkedList1.tail.next = linkedList1.head;
        System.out.println(isCircular(linkedList1));

        // Example 2
        LinkedList<Integer> linkedList2 = new LinkedList<>();
        linkedList2.build(2, 4, 6, 7, 5, 1);
        System.out.println(isCircular(linkedList2));
    }

    public static <T> boolean isCircular(LinkedList<T> linkedList) {
        /*
            Time complexity is O(1) and space complexity is O(1).
         */
        if (linkedList.length == 0) return false;
        return linkedList.tail.next == linkedList.head;
    }
}

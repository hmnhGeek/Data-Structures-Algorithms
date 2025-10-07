// Problem link - https://leetcode.com/problems/middle-of-the-linked-list/description/


package LinkedLists.Problem15;

public class Solution {
    public static <T> T getMiddle(LinkedList<T> linkedList) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        Node<T> slow = linkedList.head, fast = linkedList.head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow.data;
    }

    public static void main(String[] args) {
        test(1, 2, 3, 4, 5);
        test(1, 2, 3, 4, 5, 6);
    }

    private static <T> void test(T...args) {
        LinkedList<T> linkedList = new LinkedList<>();
        linkedList.build(args);
        System.out.println(getMiddle(linkedList));
    }
}

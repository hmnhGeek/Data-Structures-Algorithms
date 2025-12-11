// Problem link - https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1


package LinkedLists.Problem18;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(1, 2, 1, 1, 2, 1);
        System.out.println(isPalindrome(l1));
        System.out.println(l1);

        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(10, 20, 30, 40, 50);
        System.out.println(isPalindrome(l2));
        System.out.println(l2);

        LinkedList<Integer> l3 = new LinkedList<>();
        l3.build(10, 20, 40, 50);
        System.out.println(isPalindrome(l3));
        System.out.println(l3);

        LinkedList<Integer> l5 = new LinkedList<>();
        l5.build(1, 2, 1, 3, 1, 2, 1);
        System.out.println(isPalindrome(l5));
        System.out.println(l5);

        LinkedList<Integer> l6 = new LinkedList<>();
        l6.build(1, 2, 1, 3, 10, 2, 1);
        System.out.println(isPalindrome(l6));
        System.out.println(l6);
    }

    public static boolean isPalindrome(LinkedList<Integer> linkedList) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        if (linkedList.length == 0) return true;
        if (linkedList.length == 1) return true;
        Node<Integer> middleNode = linkedList.getMiddleNode();
        Node<Integer> startNode = middleNode.next;
        Node<Integer> partHead = linkedList.reverseSection(startNode);
        middleNode.next = partHead;
        Node<Integer> pointer1 = linkedList.head;
        Node<Integer> pointer2 = partHead;
        while (pointer2 != null && pointer1.data == pointer2.data) {
            pointer1 = pointer1.next;
            pointer2 = pointer2.next;
        }
        boolean flag = false;
        if (pointer2 == null) {
            flag = true;
        }
        middleNode.next = linkedList.reverseSection(partHead);
        return flag;
    }
}

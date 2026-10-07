// Problem link - https://www.geeksforgeeks.org/problems/multiply-two-linked-lists/1


package LinkedLists.Problem32;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>(), l2 = new LinkedList<>();
        l1.build(3, 2);
        l2.build(2);
        System.out.println(multiply(l1, l2));

        LinkedList<Integer> l3 = new LinkedList<>(), l4 = new LinkedList<>();
        l3.build(1, 0, 0);
        l4.build(1, 0);
        System.out.println(multiply(l3, l4));
    }

    public static Integer multiply(LinkedList<Integer> l1, LinkedList<Integer> l2) {
        /*
            Time complexity is O(max(l1, l2)) and space complexity is O(1).
         */
        if (l1 == null || l2 == null) {
            throw new IllegalArgumentException("Linked list(s) cannot be null.");
        }
        if (l1.isEmpty() || l2.isEmpty()) {
            throw new IllegalArgumentException("Linked list(s) cannot be empty.");
        }
        Integer n1 = getNumber(l1);
        Integer n2 = getNumber(l2);
        return (int) ((n1 * n2) % (Math.pow(10, 9) + 7));
    }

    private static Integer getNumber(LinkedList<Integer> linkedList) {
        if (linkedList == null || linkedList.isEmpty()) {
            throw new IllegalArgumentException("Linked list cannot be empty or null.");
        }
        Node<Integer> curr = linkedList.head;
        Integer num = 0;
        while (curr != null) {
            num = (10 * num) + curr.data;
            curr = curr.next;
        }
        return num;
    }
}

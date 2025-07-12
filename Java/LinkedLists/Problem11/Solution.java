// Problem link - https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1


package LinkedLists.Problem11;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(1, 2, 3, 4, 6);
        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(2, 4, 6, 8);
        System.out.println(intersect(l1, l2));

        LinkedList<Integer> l3 = new LinkedList<>();
        LinkedList<Integer> l4 = new LinkedList<>();
        l3.build(10, 20, 40, 50);
        l4.build(15, 40);
        System.out.println(intersect(l3, l4));
    }

    public static <T extends Comparable<T>> LinkedList<T> intersect(LinkedList<T> l1, LinkedList<T> l2) {
        /*
            Time complexity is O(n + m) and space complexity is O(1).
         */
        Node<T> curr1 = l1.getHead(), curr2 = l2.getHead();
        LinkedList<T> result = new LinkedList<>();
        while (curr1 != null && curr2 != null) {
            if (curr1.getData().compareTo(curr2.getData()) == 0) {
                result.push(curr1.getData());
                curr1 = curr1.getNext();
                curr2 = curr2.getNext();
            } else if (curr1.getData().compareTo(curr2.getData()) > 0) {
                curr2 = curr2.getNext();
            } else {
                curr1 = curr1.getNext();
            }
        }
        return result;
    }
}

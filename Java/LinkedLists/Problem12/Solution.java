// Problem link - https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1
// Solution - https://www.youtube.com/watch?v=0DYoPz2Tpt4


package LinkedLists.Problem12;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(4, 1, 8, 4, 5);
        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(5, 6, 1);
        l2.getTail().setNext(l1.getHead().getNext().getNext());
        l2.setTail(l1.getTail());
        System.out.println(l1);
        System.out.println(l2);
        System.out.println(getIntersectionPoint(l1, l2));

        LinkedList<Integer> l3 = new LinkedList<>();
        l3.build(4, 4, 4, 4, 4);
        LinkedList<Integer> l4 = new LinkedList<>();
        l4.build(4);
        l4.getTail().setNext(l3.getHead().getNext().getNext().getNext());
        l4.setTail(l3.getTail());
        System.out.println(l3);
        System.out.println(l4);
        System.out.println(getIntersectionPoint(l3, l4));
    }

    public static <T> T getIntersectionPoint(LinkedList<T> l1, LinkedList<T> l2) {
        /*
            Time complexity is O(n + m) and space complexity is O(1).
         */

        Node<T> i = l1.getHead(), j = l2.getHead();
        Integer a = 0, b = 1;
        while (i != j) {
            if (i.getNext() == null) {
                if (a == 0) {
                    i = l2.getHead();
                    a = 1;
                } else {
                    i = l1.getHead();
                    a = 0;
                }
            } else {
                i = i.getNext();
            }

            if (j.getNext() == null) {
                if (b == 1) {
                    j = l1.getHead();
                    b = 0;
                } else {
                    j = l2.getHead();
                    b = 1;
                }
            } else {
                j = j.getNext();
            }
        }
        return i.getData();
    }
}

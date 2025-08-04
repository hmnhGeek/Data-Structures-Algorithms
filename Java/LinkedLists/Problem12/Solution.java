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
    }

    public static <T> T getIntersectionPoint(LinkedList<T> l1, LinkedList<T> l2) {
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

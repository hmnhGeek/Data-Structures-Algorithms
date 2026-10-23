package LinkedLists.Problem33;

public class Solution {
    public static void main(String[] args) {
        test(1, 1, -1, 2, -10, 0);
        test(12, 15, 10, 11, 5, 6, 2, 3);
        test(10, 20, 30, 40, 50, 60);
    }

    private static void test(Integer...args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(args);
        System.out.println(linkedList);
        deleteSmallOnLeft(linkedList);
        System.out.println();
    }

    public static void deleteSmallOnLeft(LinkedList<Integer> linkedList) {
        reverse(linkedList);
        Node<Integer> curr = linkedList.head;
        Integer maxValue = Integer.MIN_VALUE;
        Node<Integer> prev = null;
        while (curr != null) {
            if (curr.data > maxValue) {
                maxValue = curr.data;
                prev = curr;
                curr = curr.next;
            } else {
                curr = delete(linkedList, prev, curr);
            }
        }
        reverse(linkedList);
        System.out.println(linkedList);
    }

    private static Node<Integer> delete(LinkedList<Integer> linkedList, Node<Integer> prev, Node<Integer> curr) {
        Node<Integer> nextCurr = curr.next;
        if (prev == null) {
            // deleting head node
            linkedList.head = linkedList.head.next;
        } else if (curr.next == null) {
            // deleting tail node
            prev.next = null;
            linkedList.tail = prev;
        } else {
            prev.next = curr.next;
        }
        linkedList.length -= 1;
        return nextCurr;
    }

    private static void reverse(LinkedList<Integer> linkedList) {
        Node<Integer> prev = null, curr = linkedList.head;
        while (curr != null) {
            Node<Integer> nextCurr = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextCurr;
        }
        Node<Integer> prevHead = linkedList.head;
        linkedList.head = linkedList.tail;
        linkedList.tail = prevHead;
    }
}

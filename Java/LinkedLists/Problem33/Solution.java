package LinkedLists.Problem33;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(1, 1, -1, 2, -10, 0);
        System.out.println(linkedList);
//        reverse(linkedList);
        delete(linkedList, linkedList.head.next.next.next.next, linkedList.head.next.next.next.next.next);
        System.out.println(linkedList);
    }

    public static void deleteSmallOnLeft(LinkedList<Integer> linkedList) {
        reverse(linkedList);
        Node<Integer> curr = linkedList.head;
        Integer maxValue = Integer.MIN_VALUE;
        Node<Integer> prev = null;
        while (curr != null) {
            if (curr.data > maxValue) {
                maxValue = curr.data;
            } else {
                delete(linkedList, prev, curr);
            }
            curr = curr.next;
        }
        reverse(linkedList);
        System.out.println(linkedList);
    }

    private static void delete(LinkedList<Integer> linkedList, Node<Integer> prev, Node<Integer> curr) {
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

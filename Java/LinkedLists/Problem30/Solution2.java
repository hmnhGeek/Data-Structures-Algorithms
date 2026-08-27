// Problem link - https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
// Solution - https://www.youtube.com/watch?v=q570bKdrnlw


package LinkedLists.Problem30;

public class Solution2 {
    public static <T> LinkedList<T> deepCopy(LinkedList<T> linkedList) {
        insertCopyNodes(linkedList);
        updateRandomPointers(linkedList);
        LinkedList<T> copied = extractCopiedLinkedList(linkedList);
        return copied;
    }

    private static <T> LinkedList<T> extractCopiedLinkedList(LinkedList<T> linkedList) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        LinkedList<T> extractedCopy = new LinkedList<>();
        Node<T> dummy = new Node<>(null);
        Node<T> temp = dummy;
        Node<T> curr = linkedList.head;
        while (curr != null) {
            temp.next = curr.next;
            curr.next = temp.next != null ? temp.next.next : null;
            temp = temp.next;
            curr = temp != null ? temp.next : null;
        }
        extractedCopy.head = dummy.next;
        extractedCopy.tail = temp;
        extractedCopy.length = linkedList.length;
        return extractedCopy;
    }

    private static <T> void updateRandomPointers(LinkedList<T> linkedList) {
        Node<T> curr = linkedList.head;
        while (curr != null) {
            Node<T> newNode = curr.next;
            Node<T> randomOfCurrNode = curr.random;
            Node<T> randomCopyNode = randomOfCurrNode != null ? randomOfCurrNode.next : null;
            newNode.random = randomCopyNode;
            curr = curr.next.next;
        }
    }

    private static <T> void insertCopyNodes(LinkedList<T> linkedList) {
        Node<T> curr = linkedList.head;
        while (curr != null) {
            Node<T> newNode = new Node<>(curr.data);
            Node<T> nextOfCurr = curr.next;
            curr.next = newNode;
            newNode.next = nextOfCurr;
            curr = curr.next.next;
        }
    }

    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(1, 2, 2, 3, -1, 10);
        linkedList.head.next.random = linkedList.tail;
        LinkedList<Integer> copied = deepCopy(linkedList);
        System.out.println(linkedList);
        System.out.println(copied);
        System.out.println(linkedList.equals(copied));
        System.out.println();

        // Example 2
        LinkedList<Integer> linkedList1 = new LinkedList<>();
        linkedList1.build(1, 3, 5, 9);
        linkedList1.head.random = linkedList1.head.next.next;
        linkedList1.head.next.random = linkedList1.head.next.next;
        linkedList1.tail.random = linkedList1.head.next.next;
        LinkedList<Integer> copied1 = deepCopy(linkedList1);
        System.out.println(linkedList1);
        System.out.println(copied1);
        System.out.println(linkedList1.equals(copied1));
        System.out.println();

        // Example 3
        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(1, 2, 3, 4, 5);
        l2.head.random = l2.head.next.next;
        l2.head.next.random = l2.head;
        l2.head.next.next.random = l2.tail;
        l2.head.next.next.next.random = l2.head.next.next;
        l2.tail.random = l2.head.next;
        LinkedList<Integer> copied2 = deepCopy(l2);
        System.out.println(l2);
        System.out.println(copied2);
        System.out.println(l2.equals(copied2));
        System.out.println();
    }
}

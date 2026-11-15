// Problem link - https://www.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1


package LinkedLists.Problem34;

public class Solution {
    public static void main(String[] args) {
        // Test case 1
        LinkedList<Integer> l1 = new LinkedList<>();
        for (int i : new int[]{17, 15, 8, 9, 2, 4, 6}) {
            l1.push(i);
        }
        System.out.println(l1);
        segregate(l1);
        System.out.println(l1);

        System.out.println();

        // Test case 2
        LinkedList<Integer> l2 = new LinkedList<>();
        for (int i : new int[]{1, 3, 5, 7}) {
            l2.push(i);
        }
        System.out.println(l2);
        segregate(l2);
        System.out.println(l2);

        System.out.println();

        // Test case 3
        LinkedList<Integer> l3 = new LinkedList<>();
        for (int i : new int[]{2, 1, 4, 8, 6, 8, 93, 94, 0}) {
            l3.push(i);
        }
        System.out.println(l3);
        segregate(l3);
        System.out.println(l3);

        System.out.println();

        // Test case 4
        LinkedList<Integer> l4 = new LinkedList<>();
        for (int i : new int[]{2, 2, 2, 0, 4, 8}) {
            l4.push(i);
        }
        System.out.println(l4);
        segregate(l4);
        System.out.println(l4);
    }

    public static void segregate(LinkedList<Integer> linkedList) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        if (linkedList.isEmpty() || linkedList.length.equals(1)) return;
        Node<Integer> evenStart = new Node<>(null);
        Node<Integer> evenTemp = evenStart;
        Node<Integer> oddStart = new Node<>(null);
        Node<Integer> oddTemp = oddStart;
        Node<Integer> curr = linkedList.head;
        while (curr != null) {
            Node<Integer> nextCurr = curr.next;
            Integer data = curr.data;
            if (data % 2 == 0) {
                evenTemp.next = curr;
                evenTemp = evenTemp.next;
            } else {
                oddTemp.next = curr;
                oddTemp = oddTemp.next;
            }
            curr.next = null;
            curr = nextCurr;
        }
        if (evenStart.next != null && oddStart.next != null) {
            evenTemp.next = oddStart.next;
            linkedList.head = evenStart.next;
            linkedList.tail = oddTemp;
        } else if (evenStart.next != null && oddStart.next == null) {
            linkedList.head = evenStart.next;
            linkedList.tail = evenTemp;
        } else if (evenStart.next == null && oddStart.next != null) {
            linkedList.head = oddStart.next;
            linkedList.tail = oddTemp;
        } else {
            // nothing to do here, if both are empty.
        }
    }
}

// Problem link - https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
// Solution - https://www.youtube.com/watch?v=ykelywHJWLg


package LinkedLists.Problem28;

public class Solution {
    private static Node<Integer> merge(Node<Integer> head1, Node<Integer> head2) {
        /*
            Time complexity is O(n * n * m) and space complexity is O(1).
         */
        Node<Integer> dummy = new Node<>(null);
        Node<Integer> temp = dummy;
        while (head1 != null && head2 != null) {
            if (head1.data <= head2.data) {
                temp.bottom = head1;
                temp = head1;
                head1 = head1.bottom;
            } else {
                temp.bottom = head2;
                temp = head2;
                head2 = head2.bottom;
            }
        }
        if (head1 == null) {
            temp.bottom = head2;
        }
        if (head2 == null) {
            temp.bottom = head1;
        }
        return dummy.bottom;
    }

    private static Node<Integer> flatten(Node<Integer> head) {
        if (head == null || head.next == null) {
            return head;
        }
        Node<Integer> head1 = flatten(head.next);
        return merge(head, head1);
    }

    public static void main(String[] args) {
        example1();
        example2();
    }

    private static void example1() {
        Node<Integer> head = new Node<>(5);
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n19 = new Node<>(19);
        Node<Integer> n28 = new Node<>(28);

        // Connect next pointers
        head.next = n10;
        n10.next = n19;
        n19.next = n28;

        // Bottom list of 5 -> 7 -> 8 -> 30
        head.bottom = new Node<>(7);
        head.bottom.bottom = new Node<>(8);
        head.bottom.bottom.bottom = new Node<>(30);

        // 10 has no bottom node

        // Bottom list of 19 -> 22 -> 50
        n19.bottom = new Node<>(22);
        n19.bottom.bottom = new Node<>(50);

        Node<Integer> flattened = flatten(head);
        Node<Integer> curr = flattened;
        while (curr != null) {
            System.out.println(curr.data);
            curr = curr.bottom;
        }
        System.out.println();
    }

    private static void example2() {
        // Top-level nodes
        Node<Integer> head = new Node<>(5);
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n19 = new Node<>(19);
        Node<Integer> n28 = new Node<>(28);

        // Connect next pointers
        head.next = n10;
        n10.next = n19;
        n19.next = n28;

        // Bottom list of 5 -> 7 -> 8
        head.bottom = new Node<>(7);
        head.bottom.bottom = new Node<>(8);

        // Bottom list of 10 -> 20
        n10.bottom = new Node<>(20);

        // Bottom list of 19 -> 22
        n19.bottom = new Node<>(22);

        // Bottom list of 28 -> 40 -> 45
        n28.bottom = new Node<>(40);
        n28.bottom.bottom = new Node<>(45);
        Node<Integer> flattened = flatten(head);
        Node<Integer> curr = flattened;
        while (curr != null) {
            System.out.println(curr.data);
            curr = curr.bottom;
        }
        System.out.println();
    }
}

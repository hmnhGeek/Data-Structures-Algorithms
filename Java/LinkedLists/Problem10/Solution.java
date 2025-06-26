// Problem link - https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

package LinkedLists.Problem10;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(4, 5);
        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(3, 4, 5);
        System.out.println(addLists(l1, l2));

        LinkedList<Integer> l3 = new LinkedList<>();
        l3.build(9, 9);
        LinkedList<Integer> l4 = new LinkedList<>();
        l4.build(9,9,9,9,9,9);
        System.out.println(addLists(l3, l4));

        LinkedList<Integer> l5 = new LinkedList<>();
        l5.build(0, 0, 6, 3);
        LinkedList<Integer> l6 = new LinkedList<>();
        l6.build(0, 7);
        System.out.println(addLists(l5, l6));
    }

    public static LinkedList<Integer> addLists(LinkedList<Integer> l1, LinkedList<Integer> l2) {
        // O(m + n) time.
        l1.reverse();
        l2.reverse();

        // initialize a carry
        int carry = 0;

        // define result linked list
        LinkedList<Integer> result = new LinkedList<>();

        // Time complexity is O(max(n, m))
        Node<Integer> curr1 = l1.getHead(), curr2 = l2.getHead();
        while (curr1 != null && curr2 != null) {
            int digit = (curr1.getData() + curr2.getData() + carry) % 10;
            carry = (curr1.getData() + curr2.getData() + carry) / 10;
            result.push(digit);
            curr1 = curr1.getNext();
            curr2 = curr2.getNext();
        }
        while (curr1 != null) {
            int digit = (curr1.getData() + carry) % 10;
            carry = (curr1.getData() + carry) / 10;
            result.push(digit);
            curr1 = curr1.getNext();
        }

        while (curr2 != null) {
            int digit = (curr2.getData() + carry) % 10;
            carry = (curr2.getData() + carry) / 10;
            result.push(digit);
            curr2 = curr2.getNext();
        }

        while (carry != 0) {
            int digit = carry % 10;
            carry = carry / 10;
            result.push(digit);
        }

        result.reverse();
        return result;
    }
}

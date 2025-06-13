// Problem link - https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1

package LinkedLists.Problem9;

public class Solution {
    public static void addOne(LinkedList<Integer> linkedList) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        linkedList.reverse();
        int carry = 1;
        Node<Integer> curr = linkedList.getHead();
        while (curr != null) {
            Integer sum = curr.getData() + carry;
            curr.setData(sum % 10);
            carry = sum / 10;
            curr = curr.getNext();
        }
        if (carry == 1) {
            linkedList.push(carry);
        }
        linkedList.reverse();
    }

    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(2,1,7,2,9,3,0,9,0,5);
        System.out.println(l1);
        addOne(l1);
        System.out.println(l1);

        System.out.println();
        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(9,9,9);
        System.out.println(l2);
        addOne(l2);
        System.out.println(l2);

        System.out.println();
        LinkedList<Integer> l3 = new LinkedList<>();
        l3.build(9);
        System.out.println(l3);
        addOne(l3);
        System.out.println(l3);
    }
}

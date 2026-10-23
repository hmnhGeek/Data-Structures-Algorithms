package LinkedLists.Problem33;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(1, 1, -1, 2, -10, 0);
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
}

package LinkedLists.Problem30;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(1, 2, 2, 3, -1, 10);
        linkedList.head.next.random = linkedList.tail;
        System.out.println(linkedList);
    }
}

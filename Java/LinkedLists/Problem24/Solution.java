package LinkedLists.Problem24;

public class Solution {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.build(1, 2, 3, 3, 4, 4, 4, 5);
        System.out.println(dll);
    }
}

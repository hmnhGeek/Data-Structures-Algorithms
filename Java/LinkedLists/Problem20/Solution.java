package LinkedLists.Problem20;

public class Solution {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.build(1, 2, 2, 3, 4, -1);
        System.out.println(dll);
    }
}

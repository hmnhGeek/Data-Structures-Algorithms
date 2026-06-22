package LinkedLists.Problem25;

public class Solution {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> db = new DoublyLinkedList<>();
        db.build(1, 2, 2, -1, -1, 0, 3, 4, 5);
        System.out.println(db);
    }
}

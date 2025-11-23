package LinkedLists.Problem17;

public class Solution {
    public static void main(String[] args) {
        CircularLinkedList<Integer> circularLinkedList = new CircularLinkedList<>();
        circularLinkedList.build(1, 2, 3, 4, 4, 5);
        System.out.println(circularLinkedList);
    }
}

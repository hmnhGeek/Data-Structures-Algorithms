package LinkedLists.Problem21;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> dll1 = new DoublyLinkedList<>();
        dll1.build(1, 5, 6);
        System.out.println(getPairs(dll1, 6));

        dll1 = new DoublyLinkedList<>();
        dll1.build(1, 2, 4, 5, 6, 8, 9);
        System.out.println(getPairs(dll1, 7));

        dll1 = new DoublyLinkedList<>();
        dll1.build(1, 2, 3, 4, 9);
        System.out.println(getPairs(dll1, 5));

        dll1 = new DoublyLinkedList<>();
        dll1.build(1, 10, 11, 12, 27);
        System.out.println(getPairs(dll1, 7));
    }

    public static List<List<Integer>> getPairs(DoublyLinkedList<Integer> dll, Integer target) {
        Node<Integer> i = dll.head, j = dll.tail;
        List<List<Integer>> result = new ArrayList<>();
        while (i != j && j.next != i) {
            int sum = i.data + j.data;
            if (sum == target) {
                result.add(List.of(i.data, j.data));
                i = i.next;
                j = j.prev;
            } else if (sum > target) {
                j = j.prev;
            } else {
                i = i.next;
            }
        }
        return result;
    }
}

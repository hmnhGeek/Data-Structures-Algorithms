package LinkedLists.Problem19;


import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        CircularLinkedList<Integer> circularLinkedList = buildList(1, 2, 3, 4);
        System.out.println(circularLinkedList);
        deleteNode(circularLinkedList, 1);
        System.out.println(circularLinkedList);
        System.out.println(circularLinkedList.head.data);
        System.out.println(circularLinkedList.tail.data);
        System.out.println(circularLinkedList.tail.next.data);
    }

    private static <T> CircularLinkedList<T> buildList(T...args) {
        CircularLinkedList<T> circularLinkedList = new CircularLinkedList<>();
        for (T arg : args) {
            circularLinkedList.push(arg);
        }
        return circularLinkedList;
    }

    public static <T> void deleteNode(CircularLinkedList<T> circularLinkedList, T item) {
        Map<String, Node<T>> map = getNode(circularLinkedList, item);
        if (map == null) return;
        Node<T> prev = map.get("prev"), curr = map.get("curr");

        if (curr == circularLinkedList.head) {
            circularLinkedList.head = curr.next;
        }
        if (curr == circularLinkedList.tail) {
            circularLinkedList.tail = prev;
        }
        prev.next = curr.next;
        circularLinkedList.length -= 1;
    }

    private static <T> Map<String, Node<T>> getNode(CircularLinkedList<T> circularLinkedList, T item) {
        if (circularLinkedList == null || circularLinkedList.isEmpty()) return null;
        Node<T> curr = circularLinkedList.head;
        Node<T> prev = circularLinkedList.tail;
        Map<String, Node<T>> map = new HashMap<>();
        while (curr != circularLinkedList.tail) {
            map.put("prev", prev);
            map.put("curr", curr);
            if (curr.data == item) {
                return map;
            }
            prev = prev.next;
            curr = curr.next;
        }
        if (circularLinkedList.tail.data == item) {
            return map;
        }
        return null;
    }
}

package LinkedLists.Problem30;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(1, 2, 2, 3, -1, 10);
        linkedList.head.next.random = linkedList.tail;
        LinkedList<Integer> copied = copyList(linkedList);
        System.out.println(linkedList);
        System.out.println(copied);
        System.out.println(linkedList.equals(copied));
    }

    public static <T> LinkedList<T> copyList(LinkedList<T> linkedList) {
        Map<Node<T>, Node<T>> map = new HashMap<>();
        LinkedList<T> resultList = buildLinearList(linkedList, map);
        updateRandomPointers(linkedList, resultList, map);
        return resultList;
    }

    private static <T> void updateRandomPointers(LinkedList<T> linkedList, LinkedList<T> resultList, Map<Node<T>, Node<T>> map) {
        Node<T> curr = linkedList.head;
        while (curr != null) {
            Node<T> originalRandomNodeAtCurr = curr.random;
            Node<T> newNodeAtCurrPlace = map.get(curr);
            Node<T> newRandomNode = map.get(originalRandomNodeAtCurr);
            newNodeAtCurrPlace.random = newRandomNode;
            curr = curr.next;
        }
    }

    private static <T> LinkedList<T> buildLinearList(LinkedList<T> linkedList, Map<Node<T>, Node<T>> map) {
        Node<T> curr = linkedList.head;
        LinkedList<T> result = new LinkedList<>();
        while (curr != null) {
            Node<T> copiedNode = result.push(curr.data);
            map.put(curr, copiedNode);
            curr = curr.next;
        }
        return result;
    }
}

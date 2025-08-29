package LinkedLists.Problem13;

import LinkedLists.Problem13.LinkedList.LinkedList;
import LinkedLists.Problem13.LinkedList.Node;

public class Solution {
    private static <T extends Comparable<T>> Node<T> getMiddleNode(LinkedList<T> linkedList) {
        Node<T> slow = linkedList.getHead();
        Node<T> fast = linkedList.getHead().getNext();
        while (fast != null && fast.getNext() != null) {
            slow = slow.getNext();
            fast = fast.getNext().getNext();
        }
        return slow;
    }
    
    public static <T extends Comparable<T>> LinkedList<T> sort(LinkedList<T> linkedList) {
        if (linkedList.getLength().equals(0) || linkedList.getLength().equals(1)) {
            return linkedList;
        }
        Node<T> midNode = getMiddleNode(linkedList);
        LinkedList<T> leftPart = new LinkedList<>();
        leftPart.setHead(linkedList.getHead());
        leftPart.setTail(midNode);
        leftPart.setLength(linkedList.getLength() % 2 == 0 ? linkedList.getLength()/2 : linkedList.getLength()/2 + 1);
        LinkedList<T> rightPart = new LinkedList<>();
        rightPart.setHead(midNode.getNext());
        rightPart.setTail(linkedList.getTail());
        rightPart.setLength(linkedList.getLength()/2);
        midNode.setNext(null);
        leftPart = sort(leftPart);
        rightPart = sort(rightPart);
        return merge(leftPart, rightPart);
    }

    private static <T extends Comparable<T>> LinkedList<T> merge(LinkedList<T> leftPart, LinkedList<T> rightPart) {
        LinkedList<T> merged = new LinkedList<>();
        Node<T> curr1 = leftPart.getHead(), curr2 = rightPart.getHead();
        while (curr1 != null && curr2 != null) {
            if (curr1.getData().compareTo(curr2.getData()) <= 0) {
                merged.push(curr1.getData());
                curr1 = curr1.getNext();
            } else {
                merged.push(curr2.getData());
                curr2 = curr2.getNext();
            }
        }
        while (curr1 != null) {
            merged.push(curr1.getData());
            curr1 = curr1.getNext();
        }
        while (curr2 != null) {
            merged.push(curr2.getData());
            curr2 = curr2.getNext();
        }
        return merged;
    }

    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(2,1,6,8,9,6,4,9,2,3,9);
        System.out.println(l1);
        l1 = sort(l1);
        System.out.println(l1);
    }
}

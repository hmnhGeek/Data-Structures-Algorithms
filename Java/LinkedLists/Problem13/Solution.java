// Problem link - https://www.geeksforgeeks.org/problems/sort-a-linked-list/1
// Solution - https://www.youtube.com/watch?v=8ocB7a_c-Cc


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
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        // if there is no node or only a single node in the linked list, return the linked list as is, because it is
        // already sorted.
        if (linkedList.getLength().equals(0) || linkedList.getLength().equals(1)) {
            return linkedList;
        }

        // get the middle node of the linked list in O(n/2) time.
        Node<T> midNode = getMiddleNode(linkedList);

        // construct the left part of the divided linked lists.
        LinkedList<T> leftPart = new LinkedList<>();
        leftPart.setHead(linkedList.getHead());
        leftPart.setTail(midNode);

        // only left part length can be asymmetrical based on the linked list's length.
        leftPart.setLength(linkedList.getLength() % 2 == 0 ? linkedList.getLength()/2 : linkedList.getLength()/2 + 1);

        // similarly, construct the right part of the linked list.
        LinkedList<T> rightPart = new LinkedList<>();
        rightPart.setHead(midNode.getNext());
        rightPart.setTail(linkedList.getTail());

        // its length will always be l/2.
        rightPart.setLength(linkedList.getLength()/2);

        // break the main linked list at mid-node.
        midNode.setNext(null);

        // sort the left and right linked lists.
        leftPart = sort(leftPart);
        rightPart = sort(rightPart);

        // finally, merge them and return the merged sorted list.
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

        LinkedList<Integer> l2 = new LinkedList<>();
        l2.build(40, 20, 60, 10, 50, 30);
        System.out.println(l2);
        l2 = sort(l2);
        System.out.println(l2);

        LinkedList<Integer> l3 = new LinkedList<>();
        l3.build(9, 5, 2, 8);
        System.out.println(l3);
        l3 = sort(l3);
        System.out.println(l3);
    }
}

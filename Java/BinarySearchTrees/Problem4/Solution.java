package BinarySearchTrees.Problem4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst1 = new BinarySearchTree<>();
        bst1.build(50, 30, 70, 20, 40, 60, 80);
        System.out.println(getPredSucc(bst1, 65));

        BinarySearchTree<Integer> bst2 = new BinarySearchTree<>();
        bst2.build(8, 1, 9, 4, 10, 3);
        System.out.println(getPredSucc(bst2, 8));
    }

    public static List<Integer> getPredSucc(BinarySearchTree<Integer> bst, Integer val) {
        Node<Integer> node = bst.getNode(bst.root, val);
        if (node == null) {
            bst.insert(val);
        }
        node = bst.getNode(bst.root, val);
        Node<Integer> predecessor = bst.getPredecessor(node);
        Node<Integer> successor = bst.getSuccessor(node);
        Integer p = predecessor != null ? predecessor.data : null;
        Integer s = successor != null ? successor.data : null;
        bst.delete(val);
        return List.of(p, s);
    }
}

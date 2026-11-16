package PracticeSet1.BinarySearchTree.Problem15;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Double> bst = new BinarySearchTree<>(6.0, 3.0, 8.0, 1.0, 4.0, 7.0, 9.0);
        System.out.println(getMedian(bst));

        bst = new BinarySearchTree<>(20.0, 8.0, 22.0, 4.0, 12.0, 10.0, 14.0);
        System.out.println(getMedian(bst));

        bst = new BinarySearchTree<>(5.0, 4.0, 8.0, 1.0);
        System.out.println(getMedian(bst));

        bst = new BinarySearchTree<>(1.0, 5.0, -10.0, 3.0, 0.0, 8.0);
        System.out.println(getMedian(bst));
    }

    private static <T extends Comparable<T>> Integer getNumNodesInBST(BinarySearchTree<T> bst) {
        List<Integer> nodesCount = Arrays.asList(0);
        getNumNodesInBST(bst.root, nodesCount);
        return nodesCount.getFirst();
    }

    private static Double getMedian(BinarySearchTree<Double> bst) {
        return getMedian(bst, (a, b) -> (a + b) / 2);
    }

    private static <T extends Comparable<T>> void getNumNodesInBST(Node<T> start, List<Integer> count) {
        if (start != null) {
            getNumNodesInBST(start.left, count);
            count.set(0, count.getFirst() + 1);
            getNumNodesInBST(start.right, count);
        }
    }

    public static <T extends Comparable<T>> T getMedian(BinarySearchTree<T> bst, BiFunction<T, T, T> averageFunction) {
        // This will take O(n) time and O(log(n)) stack space.
        Integer numNodes = getNumNodesInBST(bst);
        List<Node<T>> medianNodes = new ArrayList<>();
        List<Integer> counter = Arrays.asList(0);
        getMedian(bst.root, (numNodes / 2) + 1, counter, medianNodes);
        if (numNodes % 2 == 1) {
            return medianNodes.getLast().data;
        } else {
            return averageFunction.apply(medianNodes.getFirst().data, medianNodes.getLast().data);
        }
    }

    private static <T extends Comparable<T>> void getMedian(Node<T> root, int medianPosition, List<Integer> counter, List<Node<T>> medianNodes) {
        if (root != null) {
            getMedian(root.left, medianPosition, counter, medianNodes);
            counter.set(0, counter.getFirst() + 1);
            if (counter.getFirst().equals(medianPosition - 1) || counter.getFirst().equals(medianPosition)) {
                medianNodes.add(root);
            }
            getMedian(root.right, medianPosition, counter, medianNodes);
        }
    }
}

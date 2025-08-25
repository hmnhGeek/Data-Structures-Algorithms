// Problem link - https://www.geeksforgeeks.org/dsa/replace-every-element-with-the-least-greater-element-on-its-right/


package BinarySearchTrees.Problem17;

import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public static void main(String[] args) {
        System.out.println(replace(Arrays.asList(8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28)));
    }

    public static List<Integer> replace(List<Integer> arr) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        List<Integer> result = new ArrayList<>();
        for (int i = arr.size() - 1; i >= 0; i -= 1) {
            Node<Integer> node = bst.insert(arr.get(i));
            Node<Integer> successor = bst.getSuccessor(node);
            if (successor != null) {
                result.add(successor.getData());
            }
            else {
                result.add(-1);
            }
        }
        return result.reversed();
    }
}

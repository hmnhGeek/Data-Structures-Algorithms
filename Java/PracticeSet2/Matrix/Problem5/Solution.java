// Problem link - https://www.geeksforgeeks.org/problems/sorted-matrix2333/1


package PracticeSet2.Matrix.Problem5;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<List<Integer>> sortMatrix(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm * log(nm)) and space complexity is O(nm).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        List<Integer> flattened = flatten(mtx);
        QuickSort.sort(flattened);
        return reconstruct(flattened, n, m);
    }

    private static List<List<Integer>> reconstruct(List<Integer> flattened, int n, int m) {
        List<List<Integer>> mtx = new ArrayList<>();
        int counter = 0;
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(flattened.get(counter));
                counter += 1;
            }
            mtx.add(row);
        }
        return mtx;
    }

    private static List<Integer> flatten(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        List<Integer> flattened = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                flattened.add(mtx.get(i).get(j));
            }
        }
        return flattened;
    }

    public static void main(String[] args) {
        System.out.println(sortMatrix(
                Arrays.asList(
                        Arrays.asList(10,20,30,40),
                        Arrays.asList(15,25,35,45),
                        Arrays.asList(27,29,37,48),
                        Arrays.asList(32,33,39,50)
                )
        ));

        System.out.println(sortMatrix(
                Arrays.asList(
                        Arrays.asList(1, 5, 3),
                        Arrays.asList(2, 8, 7),
                        Arrays.asList(4, 6, 9)
                )
        ));
    }
}

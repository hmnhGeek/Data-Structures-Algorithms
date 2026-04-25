// Problem link - https://www.geeksforgeeks.org/problems/common-elements1132/1
// Solution - https://www.youtube.com/watch?v=ajWCEu1razQ


package Arrays.Problem19;

import java.util.*;

public class Solution {
    public static List<Integer> getCommonInThreeArrays(
            List<Integer> arr1, List<Integer> arr2, List<Integer> arr3
    ) {
        /*
            Time complexity is O(n1 + n2 + n3) and space complexity is O(1).
         */
        int n1 = arr1.size(), n2 = arr2.size(), n3 = arr3.size();
        int i = 0, j = 0, k = 0;
        List<Integer> result = new ArrayList<>();
        while (i < n1 && j < n2 && k < n3) {
            if (Objects.equals(arr1.get(i), arr2.get(j)) && Objects.equals(arr2.get(j), arr3.get(k))) {
                result.add(arr1.get(i));
                i += 1;
                j += 1;
                k += 1;
                i = update(arr1, i, n1);
                j = update(arr2, j, n2);
                k = update(arr3, k, n3);
            } else if (arr1.get(i) < arr2.get(j)) {
                i += 1;
                i = update(arr1, i, n1);
            } else if (arr2.get(j) < arr3.get(k)) {
                j += 1;
                j = update(arr2, j, n2);
            } else {
                k += 1;
                k = update(arr3, k, n3);
            }
        }
        return result;
    }

    private static int update(List<Integer> arr1, int i, int n1) {
        Integer prev1 = arr1.get(i - 1);
        while (i < n1 && Objects.equals(prev1, arr1.get(i))) {
            i += 1;
        }
        return i;
    }

    public static void main(String[] args) {

        System.out.println(
                getCommonInThreeArrays(
                        Arrays.asList(1, 5, 10, 20, 40, 80),
                        Arrays.asList(6, 7, 20, 80, 100),
                        Arrays.asList(3, 4, 15, 20, 30, 70, 80, 120)
                )
        );

        System.out.println(
                getCommonInThreeArrays(
                        Arrays.asList(1, 2, 3, 4, 5),
                        Arrays.asList(6, 7),
                        Arrays.asList(8, 9, 10)
                )
        );

        System.out.println(
                getCommonInThreeArrays(
                        Arrays.asList(1, 1, 1, 2, 2, 2),
                        Arrays.asList(1, 1, 2, 2, 2),
                        Arrays.asList(1, 1, 1, 1, 2, 2, 2, 2)
                )
        );

        System.out.println(
                getCommonInThreeArrays(
                        Arrays.asList(1, 5, 10, 20, 30),
                        Arrays.asList(5, 13, 15, 20),
                        Arrays.asList(5, 20)
                )
        );

        System.out.println(
                getCommonInThreeArrays(
                        Arrays.asList(2, 5, 10, 30),
                        Arrays.asList(5, 20, 34),
                        Arrays.asList(5, 13, 19)
                )
        );

        System.out.println(
                getCommonInThreeArrays(
                        Arrays.asList(2, 3, 4, 7),
                        Arrays.asList(0, 0, 3, 5),
                        Arrays.asList(1, 3, 8, 9)
                )
        );
    }
}

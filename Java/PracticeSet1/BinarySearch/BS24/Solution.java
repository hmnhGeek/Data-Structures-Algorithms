// Problem link - https://leetcode.com/problems/search-a-2d-matrix/
// Solution - https://www.youtube.com/watch?v=JXU4Akft7yk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=26


package PracticeSet1.BinarySearch.BS24;

import java.util.List;

public class Solution {
    public static List<Integer> search(List<List<Integer>> mtx, Integer target) {
        /*
            Time complexity is O(log(mn)) and space complexity is O(1).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        int low = 0, high = (n * m) - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int i = mid / m, j = mid % m;
            if (mtx.get(i).get(j).equals(target)) {
                return List.of(i, j);
            } else if (mtx.get(i).get(j).compareTo(target) > 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return null;
    }

    public static void main(String[] args) {

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(3, 4, 7, 9),
                                List.of(12, 13, 16, 18),
                                List.of(20, 21, 23, 29)
                        ),
                        23
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(3, 4, 7, 9),
                                List.of(12, 13, 16, 18),
                                List.of(20, 21, 23, 29)
                        ),
                        28
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(1, 3, 5, 7),
                                List.of(10, 11, 16, 20),
                                List.of(23, 30, 34, 60)
                        ),
                        3
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(1, 3, 5, 7),
                                List.of(10, 11, 16, 20),
                                List.of(23, 30, 34, 60)
                        ),
                        13
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(18, 21, 27),
                                List.of(38, 55, 67)
                        ),
                        55
                )
        );
    }
}

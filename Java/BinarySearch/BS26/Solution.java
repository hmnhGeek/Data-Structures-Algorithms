// Problem link - https://www.geeksforgeeks.org/find-peak-element-2d-array/
// Solution - https://www.youtube.com/watch?v=nGGp5XBzC4g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=28

package BinarySearch.BS26;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                findPeak(
                        Arrays.asList(
                                Arrays.asList(4, 2, 5, 1, 4, 5),
                                Arrays.asList(2, 9, 3, 2, 3, 2),
                                Arrays.asList(1, 7, 6, 0, 1, 3),
                                Arrays.asList(3, 6, 2, 3, 7, 2)
                        )
                )
        );

        System.out.println(
                findPeak(
                        Arrays.asList(
                                Arrays.asList(1, 4),
                                Arrays.asList(3, 2)
                        )
                )
        );

        System.out.println(
                findPeak(
                        Arrays.asList(
                                Arrays.asList(10, 20, 15),
                                Arrays.asList(21, 30, 14),
                                Arrays.asList(7, 16, 32)
                        )
                )
        );

        System.out.println(
                findPeak(
                        Arrays.asList(
                                Arrays.asList(10, 7),
                                Arrays.asList(11, 17)
                        )
                )
        );
    }

    public static Integer findPeak(List<List<Integer>> mtx) {
        /*
            Time complexity is O(n * log(m)) and space complexity is O(1).
         */

        // get matrix size
        int n = mtx.size(), m = mtx.getFirst().size();

        // define search space on columns
        int low = 0, high = m - 1;

        // typical binary search...
        while (low <= high) {
            int mid = (low + (high - low)/2);

            // get the maximum element in the column in O(n) time.
            int maxElementIndex = getMaxElementIndex(mtx, mid, n);

            // reduce the search space.
            if (maxElementIndex == 0) {
                if (mid == 0) {
                    if (mtx.get(maxElementIndex).get(mid + 1) > mtx.get(maxElementIndex).get(mid)) {
                        low = mid + 1;
                    } else {
                        return mtx.get(maxElementIndex).get(mid);
                    }
                } else if (mid == m - 1) {
                    if (mtx.get(maxElementIndex).get(mid - 1) > mtx.get(maxElementIndex).get(mid)) {
                        high = mid - 1;
                    } else {
                        return mtx.get(maxElementIndex).get(mid);
                    }
                } else {
                    if (mtx.get(maxElementIndex).get(mid) > mtx.get(maxElementIndex).get(mid - 1) && mtx.get(maxElementIndex).get(mid) > mtx.get(maxElementIndex).get(mid + 1)) {
                        return mtx.get(maxElementIndex).get(mid);
                    } else if (mtx.get(maxElementIndex).get(mid) < mtx.get(maxElementIndex).get(mid + 1)) {
                        low = mid + 1;
                    } else if (mtx.get(maxElementIndex).get(mid) < mtx.get(maxElementIndex).get(mid - 1)) {
                        high = mid - 1;
                    } else {
                        high = mid - 1;
                    }
                }
            } else if (maxElementIndex == n - 1) {
                if (mid == 0) {
                    if (mtx.get(maxElementIndex).get(mid + 1) > mtx.get(maxElementIndex).get(mid)) {
                        low = mid + 1;
                    } else {
                        return mtx.get(maxElementIndex).get(mid);
                    }
                } else if (mid == m - 1) {
                    if (mtx.get(maxElementIndex).get(mid - 1) > mtx.get(maxElementIndex).get(mid)) {
                        high = mid - 1;
                    } else {
                        return mtx.get(maxElementIndex).get(mid);
                    }
                } else {
                    if (mtx.get(maxElementIndex).get(mid) > mtx.get(maxElementIndex).get(mid - 1) && mtx.get(maxElementIndex).get(mid) > mtx.get(maxElementIndex).get(mid + 1)) {
                        return mtx.get(maxElementIndex).get(mid);
                    } else if (mtx.get(maxElementIndex).get(mid) < mtx.get(maxElementIndex).get(mid + 1)) {
                        low = mid + 1;
                    } else if (mtx.get(maxElementIndex).get(mid) < mtx.get(maxElementIndex).get(mid - 1)) {
                        high = mid - 1;
                    } else {
                        high = mid - 1;
                    }
                }
            } else {
                if (mtx.get(maxElementIndex).get(mid) > mtx.get(maxElementIndex).get(mid - 1) && mtx.get(maxElementIndex).get(mid) > mtx.get(maxElementIndex).get(mid + 1)) {
                    return mtx.get(maxElementIndex).get(mid);
                } else if (mtx.get(maxElementIndex).get(mid) < mtx.get(maxElementIndex).get(mid + 1)) {
                    low = mid + 1;
                } else if (mtx.get(maxElementIndex).get(mid) < mtx.get(maxElementIndex).get(mid - 1)) {
                    high = mid - 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }

    private static Integer getMaxElementIndex(List<List<Integer>> mtx, int mid, int n) {
        Integer maxElement = Integer.MIN_VALUE;
        Integer index = -1;
        for (int i = 0; i < n; i += 1) {
            if (mtx.get(i).get(mid) > maxElement) {
                maxElement = mtx.get(i).get(mid);
                index = i;
            }
        }
        return index;
    }
}

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
    }

    public static Integer findPeak(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        int low = 0, high = m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int maxElementIndex = getMaxElementIndex(mtx, mid, n);
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

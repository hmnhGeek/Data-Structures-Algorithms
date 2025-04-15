package BinarySearch;


import java.util.Arrays;
import java.util.List;

class SolutionBS22 {
    private static Integer getKthElement(List<Integer> arr1, List<Integer> arr2, Integer k) {
        int n1 = arr1.size(), n2 = arr2.size();
        if (n1 > n2) {
            return getKthElement(arr2, arr1, k);
        }
        int high = Math.min(k, n1);
        int low = Math.max(k - n2, 0);
        int left = k;
        int n = n1 + n2;
        while (low <= high) {
            int mid1 = low + (high - low)/2;
            int mid2 = k - mid1;
            int l1 = 0 <= mid1 - 1 && mid1 - 1 < n1 ? arr1.get(mid1 - 1) : Integer.MIN_VALUE;
            int l2 = 0 <= mid2 - 1 && mid2 - 1 < n2 ? arr2.get(mid2 - 1) : Integer.MIN_VALUE;
            int r1 = 0 <= mid1 && mid1 < n1 ? arr1.get(mid1) : Integer.MAX_VALUE;
            int r2 = 0 <= mid2 && mid2 < n2 ? arr2.get(mid2) : Integer.MAX_VALUE;
            if (l1 > r2) {
                high = mid1 - 1;
            } else if (l2 > r1) {
                low = mid1 + 1;
            } else {
                return Math.max(l1, l2);
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(SolutionBS22.getKthElement(Arrays.asList(2, 3, 6, 7, 9), Arrays.asList(1, 4, 8, 10), 4));
    }
}
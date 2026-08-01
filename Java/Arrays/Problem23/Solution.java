// Problem link - https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1
// Solution - https://www.youtube.com/watch?v=hnswaLJvr6g


package Arrays.Problem23;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getMaxProduct(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = arr.size();
        int maxProduct = Integer.MIN_VALUE;
        int prefix = 1, suffix = 1;
        for (int i = 0; i < n; i += 1) {
            if (prefix == 0) {
                prefix = 1;
            }
            if (suffix == 0) {
                suffix = 1;
            }
            prefix = prefix * arr.get(i);
            suffix = suffix * arr.get(n - i - 1);
            maxProduct = Math.max(maxProduct, Math.max(prefix, suffix));
        }
        return maxProduct;
    }

    public static void main(String[] args) {
        System.out.println(getMaxProduct(Arrays.asList(-2, 6, -3, -10, 0, 2)));
        System.out.println(getMaxProduct(Arrays.asList(-1, -3, -10, 0, 6)));
        System.out.println(getMaxProduct(Arrays.asList(2, 3, 4)));
        System.out.println(getMaxProduct(Arrays.asList(2, 3, -2, 4)));
        System.out.println(getMaxProduct(Arrays.asList(-2, 0, -1)));
        System.out.println(getMaxProduct(Arrays.asList(1, 2, 3, 4, 5, 0)));
        System.out.println(getMaxProduct(Arrays.asList(1, 2, -3, 0, -4, -5)));
    }
}

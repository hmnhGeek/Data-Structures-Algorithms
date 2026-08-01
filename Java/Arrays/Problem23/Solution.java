package Arrays.Problem23;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getMaxProduct(List<Integer> arr) {
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
    }
}

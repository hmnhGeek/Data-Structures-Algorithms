package SearchingAndSorting.Problem11;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getFourSum(Arrays.asList(0, 0, 2, 1, 1), 3));
    }

    public static List<List<Integer>> getFourSum(List<Integer> arr, Integer target) {
        QuickSort.sort(arr);
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < arr.size(); i += 1) {
            if (i > 0 && Objects.equals(arr.get(i - 1), arr.get(i))) continue;
            for (int j = i + 1; j < arr.size(); j += 1) {
                if (j != i + 1 && Objects.equals(arr.get(j - 1), arr.get(j))) continue;
                int k = j + 1, l = arr.size() - 1;
                while (k < l) {
                    Integer sum = arr.get(i) + arr.get(j) + arr.get(k) + arr.get(l);
                    if (sum.equals(target)) {
                        result.add(Arrays.asList(arr.get(i), arr.get(j), arr.get(k), arr.get(l)));
                        k += 1;
                        l -= 1;
                        while (k < l && Objects.equals(arr.get(k - 1), arr.get(k))) {
                            k += 1;
                        }
                        while (k < l && Objects.equals(arr.get(l + 1), arr.get(l))) {
                            l -= 1;
                        }
                    } else if (sum.compareTo(target) > 0) {
                        l -= 1;
                    } else {
                        k += 1;
                    }
                }
            }
        }
        return result;
    }
}

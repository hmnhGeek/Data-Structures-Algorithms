package SearchingAndSorting.Problem9;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class Solution {
    public static void main(String[] args) {
        System.out.println(search(Arrays.asList(4, 5, 6, 7, 6), 6, 1));
        System.out.println(search(Arrays.asList(20, 40, 50, 70, 70, 60), 60, 20));
    }

    public static Integer search(List<Integer> arr, Integer x, Integer k) {
        int i = 0;
        while (i < arr.size()){
            if (Objects.equals(arr.get(i), x)) {
                return i;
            }
            i = i + Math.max(Math.abs(arr.get(i) - x)/k, 1);
        }
        return null;
    }
}

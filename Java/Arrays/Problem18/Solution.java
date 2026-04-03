package Arrays.Problem18;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<Integer> a = Arrays.asList(2, 6, 8, 0, 9, 9, 7);
        QuickSort.sort(a);
        System.out.println(a);
    }
}

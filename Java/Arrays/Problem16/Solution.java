package Arrays.Problem16;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(MergeSort.getInversionCount(Arrays.asList(2, 4, 1, 3, 5)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(2, 3, 4, 5, 6)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(10, 10, 10)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(4, 3, 2, 1)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(5, 4, 3, 2, 1)));
    }
}

// Problem link - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
// Solution - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1


package Arrays.Problem16;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(MergeSort.getInversionCount(Arrays.asList(2, 4, 1, 3, 5)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(2, 3, 4, 5, 6)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(10, 10, 10)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(4, 3, 2, 1)));
        System.out.println(MergeSort.getInversionCount(Arrays.asList(5, 4, 3, 2, 1)));
    }
}

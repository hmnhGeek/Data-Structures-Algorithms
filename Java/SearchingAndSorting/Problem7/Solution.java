package SearchingAndSorting.Problem7;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getMissingAndRepeating(Arrays.asList(2, 2)));
        System.out.println(getMissingAndRepeating(Arrays.asList(1, 3, 3)));
        System.out.println(getMissingAndRepeating(Arrays.asList(4, 3, 6, 2, 1, 1)));
        System.out.println(getMissingAndRepeating(Arrays.asList(1, 2, 3, 4, 4, 5)));
        System.out.println();
    }

    public static List<Integer> getMissingAndRepeating(List<Integer> arr) {
        int n = arr.size();
        List<Integer> sums = getSumOfArray(arr, n);
        Integer sigma = sums.getFirst();
        Integer rho = sums.getLast();
        Integer sum = n*(n + 1)/2;
        Integer sn = n*(n + 1)*(2*n + 1)/6;
        Integer missingNumber = (((rho - sn)/(sigma - sum)) + sum - sigma)/2;
        Integer repeatingNumber = missingNumber - sum + sigma;
        return List.of(missingNumber, repeatingNumber);
    }

    private static List<Integer> getSumOfArray(List<Integer> arr, int n) {
        int sum = 0;
        int sumOfSquares = 0;
        for (Integer i : arr) {
            sum += i;
            sumOfSquares += (i * i);
        }
        return List.of(sum, sumOfSquares);
    }
}

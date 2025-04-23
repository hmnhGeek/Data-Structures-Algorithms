package SearchingAndSorting.Problem29;

public class Solution {
    private static Integer getNumTrailingZerosInFactorialOf(Integer n) {
        int x = (int) Math.ceil(Math.log(n)/Math.log(5));
        int numZeros = 0;
        for (int i = 1; i <= x; i += 1) {
            numZeros += (int) Math.floor(n/Math.pow(5, i));
        }
        return numZeros;
    }

    public static Integer smallestFactorialNumber(Integer numTrailingZeros) {
        int low = 0, high = 10000;
        while(low <= high) {
            int mid = (low + (high - low)/2);
            Integer numZeros = getNumTrailingZerosInFactorialOf(mid);
            if (numZeros > numTrailingZeros) {
                high = mid - 1;
            } else if (numZeros.equals(numTrailingZeros)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    public static void main(String[] args) {
        System.out.println(smallestFactorialNumber(6));
        System.out.println(smallestFactorialNumber(1));
    }
}

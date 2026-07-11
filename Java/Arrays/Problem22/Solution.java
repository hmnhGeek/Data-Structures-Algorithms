package Arrays.Problem22;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<Integer> getFactorial(Integer n) {
        List<Integer> result = new ArrayList<>();
        result.add(1);

        // base case of any factorial, no computation is needed.
        if (n == 0 || n == 1) return result;

        // variable to carry forward the carry value of multiplication.
        int carry = 0;

        // simple factorial condition
        while (n != 1) {
            // since we cannot modify the `result` list as it is being used in for-loop, we use a temporary
            // sublist to update and store the multiplication.
            List<Integer> subList = new ArrayList<>();

            // loop on the result list.
            for (int i = 0; i < result.size(); i += 1) {
                // get the current multiplication at `i` index.
                int num = (result.get(i) * n) + carry;

                // get the unit digit and add it to temp list
                int unitDigit = num % 10;
                subList.add(unitDigit);

                // update the carry value.
                carry = num / 10;
            }

            // up until carry becomes 0, continue to add in temp list.
            while (carry != 0) {
                subList.add(carry % 10);
                carry = carry / 10;
            }

            // update result and n value.
            result = subList;
            n -= 1;
        }

        // return the reversed version of result which contains the final factorial value.
        return result.reversed();
    }

    public static void main(String[] args) {
        System.out.println(getFactorial(5));
        System.out.println(getFactorial(10));
    }
}

package Arrays.Problem22;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<Integer> getFactorial(Integer n) {
        List<Integer> result = new ArrayList<>();
        result.add(1);
        if (n == 0 || n == 1) return result;
        int carry = 0;
        while (n != 1) {
            List<Integer> subList = new ArrayList<>();
            for (int i = 0; i < result.size(); i += 1) {
                int num = (result.get(i) * n) + carry;
                int unitDigit = num % 10;
                subList.add(unitDigit);
                carry = num / 10;
            }
            while (carry != 0) {
                subList.add(carry % 10);
                carry = carry / 10;
            }
            result = subList;
            n -= 1;
        }
        return result.reversed();
    }

    public static void main(String[] args) {
        System.out.println(getFactorial(5));
        System.out.println(getFactorial(10));
    }
}

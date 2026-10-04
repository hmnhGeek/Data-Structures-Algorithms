package SearchingAndSorting.Problem16;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getProductExceptSelf(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        result.add(1);
        for (int i = 1; i < arr.size(); i += 1) {
            result.add(result.get(i - 1) * arr.get(i - 1));
        }
        int rightProduct = 1;
        for (int i = arr.size() - 1; i >= 0; i -= 1) {
            result.set(i, result.get(i) * rightProduct);
            rightProduct *= arr.get(i);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getProductExceptSelf(Arrays.asList(1, 2, 3, 4)));
        System.out.println(getProductExceptSelf(Arrays.asList(12, 0)));
        System.out.println(getProductExceptSelf(Arrays.asList(10, 3, 5, 6, 2)));
        System.out.println(getProductExceptSelf(Arrays.asList(1, 0, 0, 3)));
    }
}

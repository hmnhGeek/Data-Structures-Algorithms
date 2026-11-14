package SearchingAndSorting.Problem37;

import java.util.ArrayList;
import java.util.List;

public class BetterSolution {
    public static List<Integer> solve(List<Integer> arr) {
        int n = arr.size();
        List<Integer> res = new ArrayList<>();
        productAndCountOfZeros result = getProductAndCountOfZeros(arr, n);
        for (int i = 0; i < n; i += 1) {
            if (arr.get(i).equals(0)) {
                if (result.countOfZeros > 1) {
                    res.add(0);
                } else {
                    res.add(result.product);
                }
            } else {
                if (result.countOfZeros > 0) {
                    res.add(0);
                } else {
                    res.add(result.product/arr.get(i));
                }
            }
        }
        return res;
    }

    private static productAndCountOfZeros getProductAndCountOfZeros(List<Integer> arr, int n) {
        int product = 1, countOfZeros = 0;
        for (int i = 0; i < n; i += 1) {
            if (arr.get(i).equals(0)) {
                countOfZeros += 1;
            } else {
                product = product * arr.get(i);
            }
        }
        productAndCountOfZeros result = new productAndCountOfZeros(product, countOfZeros);
        return result;
    }

    private record productAndCountOfZeros(int product, int countOfZeros) {
    }
}

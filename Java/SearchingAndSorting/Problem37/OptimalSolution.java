package SearchingAndSorting.Problem37;

import java.util.ArrayList;
import java.util.List;

public class OptimalSolution {
    public static List<Integer> solve(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        int prefixMultiplier = 1;
        for (int i = 0; i < arr.size(); i += 1) {
            result.add(prefixMultiplier);
            prefixMultiplier = prefixMultiplier * arr.get(i);
        }
        int suffixMultiplier = 1;
        for (int i = arr.size() - 1; i >= 0; i -= 1) {
            result.set(i, suffixMultiplier * result.get(i));
            suffixMultiplier = suffixMultiplier * arr.get(i);
        }
        return result;
    }
}

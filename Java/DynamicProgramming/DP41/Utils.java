package DynamicProgramming.DP41;

import java.util.List;

public class Utils {
    public static Integer getValAtIdx(List<Integer> arr, int j, int n) {
        if (j >= n) return Integer.MAX_VALUE;
        return arr.get(j);
    }
}

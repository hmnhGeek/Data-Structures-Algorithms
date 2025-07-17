package DynamicProgramming.DP7;

import java.util.List;

public class Utils {
    public static List<Integer> getNext(int i) {
        if (i == 0) return List.of(1, 2);
        if (i == 1) return List.of(0, 2);
        return List.of(0, 1);
    }
}

package Matrix.Problem8;

import java.util.List;

public class Utils {
    public static <T> void transpose(List<List<T>> mtx) {
        int n = mtx.size();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < n - i; j += 1) {
                T val = mtx.get(i).get(j);
                mtx.get(i).set(j, mtx.get(j).get(i));
                mtx.get(j).set(i, val);
            }
        }
    }
}

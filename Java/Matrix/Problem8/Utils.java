package Matrix.Problem8;

import java.util.Collections;
import java.util.List;

public class Utils {
    public static <T> void transpose(List<List<T>> mtx) {
        int n = mtx.size();
        for (int i = 0; i < n; i += 1) {
            for (int j = i; j < n; j += 1) {
                T val = mtx.get(i).get(j);
                mtx.get(i).set(j, mtx.get(j).get(i));
                mtx.get(j).set(i, val);
            }
        }
    }

    public static <T> void lateralInvert(List<List<T>> mtx) {
        int n = mtx.size();
        int i = 0;
        while (i < n) {
            int x = 0, y = n - 1;
            while (x <= y) {
                Collections.swap(mtx.get(i), x, y);
                x += 1;
                y -= 1;
            }
            i += 1;
        }
    }
}

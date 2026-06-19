// LPS Solution is also in this video - https://www.youtube.com/watch?v=qases-9gOpk

package Strings.Problem19;

import java.util.ArrayList;
import java.util.List;

public class Utils {
    public static List<Integer> getLPS(String string) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = string.length();
        List<Integer> lps = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            lps.add(null);
        }
        lps.set(0, 0); // lps[0] is always 0.
        int length = 0;
        int i = 1;
        while (i < n) {
            if (string.charAt(length) == string.charAt(i)) {
                length += 1;
                lps.set(i, length);
                i += 1;
            } else if (string.charAt(lps.get(length)) != string.charAt(i)) {
                if (length - 1 >= 0) {
                    length = lps.get(length - 1);
                } else {
                    length = 0;
                    lps.set(i, length);
                    i += 1;
                }
            }
        }
        return lps;
    }
}

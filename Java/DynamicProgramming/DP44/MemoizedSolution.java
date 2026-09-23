//package DynamicProgramming.DP44;
//
//import java.util.List;
//import java.util.Map;
//
//public class MemoizedSolution {
//    public static Integer getLDSLength(List<Integer> arr) {
//        /*
//            Time complexity is exponential and space complexity is O(n).
//         */
//        int n = arr.size();
//        Map
//        return solve(arr, n - 1, null);
//    }
//
//    private static Integer solve(List<Integer> arr, int i, Integer prev) {
//        if (i == 0) {
//            if (prev == null) return 1;
//            if (arr.get(i) % prev == 0 || prev % arr.get(i) == 0) {
//                return 1;
//            }
//            return 0;
//        }
//
//        if (prev == null) {
//            return Math.max(
//                    1 + solve(arr, i - 1, arr.get(i)),
//                    solve(arr, i - 1, null)
//            );
//        }
//        Integer left = Integer.MIN_VALUE;
//        if (arr.get(i) % prev == 0 || prev % arr.get(i) == 0) {
//            left = 1 + solve(arr, i - 1, arr.get(i));
//        }
//        Integer right = solve(arr, i - 1, prev);
//        return Math.max(left, right);
//    }
//}

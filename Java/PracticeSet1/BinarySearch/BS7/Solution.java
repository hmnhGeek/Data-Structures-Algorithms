// Problem link - https://www.naukri.com/code360/problems/rotation_7449070
// Solution - https://www.youtube.com/watch?v=jtSiWTPLwd0&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=8


package PracticeSet1.BinarySearch.BS7;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getNumRotations(List<Integer> arr) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        int n = arr.size();
        int low = 0, high = n - 1;
        Integer ans = 0;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(low) == arr.get(mid) && arr.get(mid) == arr.get(high)) {
                if (arr.get(low) < arr.get(ans)) {
                    ans = low;
                }
                low += 1;
                high -= 1;
                continue;
            }
            if (arr.get(low) <= arr.get(mid)) {
                if (arr.get(low) < arr.get(ans)) {
                    ans = low;
                }
                low = mid + 1;
            } else {
                if (arr.get(mid) < arr.get(ans)) {
                    ans = mid;
                }
                high = mid - 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(getNumRotations(Arrays.asList(3, 4, 5, 1, 2)));
        System.out.println(getNumRotations(Arrays.asList(1, 2, 4, 5, 7)));
        System.out.println(getNumRotations(Arrays.asList(3, 3, 3, 3, 2, 3, 3)));
        System.out.println(getNumRotations(Arrays.asList(1, 2, 3)));
        System.out.println(getNumRotations(Arrays.asList(2, 3, 4, 1)));
    }
}

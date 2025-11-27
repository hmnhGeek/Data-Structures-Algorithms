package BinarySearch.BS15;

import java.util.Collections;
import java.util.List;

public class Solution {
    private static Integer getSum(List<Integer> arr) {
        Integer result = 0;
        for (Integer i : arr) {
            result += i;
        }
        return result;
    }

    public static Integer getLeastShipCapacity(List<Integer> items, Integer daysUpperLimit) {
        if (daysUpperLimit <= 0) return null;
        int low = Collections.max(items), high = getSum(items);
        while (low <= high) {
            int mid = (low + (high - low)/2);
            Integer numDaysTakenToShipAll = findDaysToShipAll(items, mid);
            if (numDaysTakenToShipAll > daysUpperLimit) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private static Integer findDaysToShipAll(List<Integer> items, int shipCapacity) {
        Integer daysTakenToShipAll = 0;
        Integer usedCapacityOfShip = 0;
        for (int i = 0; i < items.size(); i += 1) {
            usedCapacityOfShip += items.get(i);
            if (usedCapacityOfShip > shipCapacity) {
                daysTakenToShipAll += 1;
                usedCapacityOfShip = items.get(i); // this will never be greater than mid (shipCapacity) as low is taken
                // to be the max value from the array. So shipCapacity, will always be >= low (max item in list).
            }
        }
        if (usedCapacityOfShip > 0) {
            daysTakenToShipAll += 1;
            usedCapacityOfShip = 0;
        }
        return daysTakenToShipAll;
    }

    public static void main(String[] args) {
        System.out.println(Solution.getLeastShipCapacity(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 5));
        System.out.println(Solution.getLeastShipCapacity(List.of(5, 4, 5, 2, 3, 4, 5, 6), 5));
        System.out.println(Solution.getLeastShipCapacity(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 1));
        System.out.println(Solution.getLeastShipCapacity(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 0));
        System.out.println(Solution.getLeastShipCapacity(List.of(3, 2, 2, 4, 1, 4), 3));
        System.out.println(Solution.getLeastShipCapacity(List.of(1, 2, 3, 1, 1), 4));
    }
}

// Problem link - https://www.geeksforgeeks.org/dsa/optimum-location-point-minimize-total-distance/


package SearchingAndSorting.Problem6;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static double getMinDistance(Line line, List<Point> points) {
        /*
            Time complexity is O(n^2) and space complexity is O(n).
         */
        double eps = 1e-9;
        double low = -1e6;
        double high = 1e6;
        while (high - low > eps) {
            double mid1 = (low + (high - low)/3);
            double mid2 = (high - (high - low)/3);
            double distance1 = getSummedDistanceOfAllPoints(line, points, mid1);
            double distance2 = getSummedDistanceOfAllPoints(line, points, mid2);
            if (distance1 < distance2) {
                high = mid2;
            } else {
                low = mid1;
            }
        }
        return getSummedDistanceOfAllPoints(line, points, (low + high)/2);
    }

    private static double getSummedDistanceOfAllPoints(Line line, List<Point> points, double xCoordinateOnLine) {
        double yCoordinateOnLine = -(line.c + line.a*xCoordinateOnLine)/line.b;
        Point linePoint = new Point(xCoordinateOnLine, yCoordinateOnLine);
        double summedDistance = 0.0;
        for (Point point : points) {
            summedDistance += Utility.getDistanceBetween(point, linePoint);
        }
        return summedDistance;
    }

    public static void main(String[] args) {
        System.out.println(
                getMinDistance(
                        new Line(1, -1, -3),
                        Arrays.asList(
                                new Point(-3.0, -2.0),
                                new Point(-1.0, 0.0),
                                new Point(-1.0, 2.0),
                                new Point(1.0, 2.0),
                                new Point(3.0, 4.0)
                        )
                )
        );
    }
}

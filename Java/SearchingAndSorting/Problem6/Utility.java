package SearchingAndSorting.Problem6;

public class Utility {
    public static Double getDistanceBetween(Point a, Point b) {
        return Math.sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y));
    }

    public static Double getDistanceFromLine(Point point, Line line) {
        Double numerator = Math.abs(point.x*line.a + point.y*line.b + line.c);
        Double denominator = Math.sqrt(line.a*line.a + line.b*line.b);
        return numerator/denominator;
    }
}

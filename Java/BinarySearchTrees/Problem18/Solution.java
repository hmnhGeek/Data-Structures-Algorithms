// Problem link - https://www.geeksforgeeks.org/dsa/given-n-appointments-find-conflicting-appointments/


package BinarySearchTrees.Problem18;

import java.util.Arrays;
import java.util.List;


class Appointment {
    public Integer startTime;
    public Integer endTime;

    public Appointment(Integer startTime, Integer endTime) {
        this.startTime = startTime;
        this.endTime = endTime;
    }

    @Override
    public String toString() {
        return String.format("[%d, %d]", startTime, endTime);
    }
}


public class Solution {
    public static void main(String[] args) {
        printConflictingAppointments(Arrays.asList(
                new Appointment(1, 5),
                new Appointment(3, 7),
                new Appointment(2, 6),
                new Appointment(10, 15),
                new Appointment(5, 6),
                new Appointment(4, 100)
        ));
    }

    public static void printConflictingAppointments(List<Appointment> appointments) {
        /*
            Time complexity is O(n^2) and space complexity is O(1).
         */
        for (int i = 1; i < appointments.size(); i += 1) {
            Appointment currentAppointment = appointments.get(i);
            for (int j = i - 1; j >= 0; j -= 1) {
                Appointment previousAppointment = appointments.get(j);
                if (
                        previousAppointment.startTime < currentAppointment.endTime
                ) {
                    System.out.println(String.format("Appointment %s conflicts with appointment %s", currentAppointment, previousAppointment));
                }
            }
        }
    }
}

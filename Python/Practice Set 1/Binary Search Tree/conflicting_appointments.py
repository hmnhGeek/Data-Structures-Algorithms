class Appointment:
    def __init__(self, s, e):
        self.start_time = s
        self.end_time = e

    def __str__(self):
        return f"[{self.start_time}, {self.end_time}]"


class Solution:
    @staticmethod
    def find_conflicting_appointments(appointments):
        for i in range(1, len(appointments)):
            appointment = appointments[i]
            for j in range(i - 1, -1, -1):
                previous_appointment = appointments[j]
                if previous_appointment.start_time < appointment.end_time:
                    print(f"Appointment {appointment} conflicts with appointment {previous_appointment}")


appointments = [
    Appointment(1, 5),
    Appointment(3, 7),
    Appointment(2, 6),
    Appointment(10, 15),
    Appointment(5, 6),
    Appointment(4, 100)
]
Solution.find_conflicting_appointments(appointments)

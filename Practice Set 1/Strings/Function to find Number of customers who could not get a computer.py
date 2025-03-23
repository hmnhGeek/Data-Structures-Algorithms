class Solution:
    @staticmethod
    def get_no_computer_customers(num_computers, customers):
        available_computers = num_computers

        timings = {}
        for customer in customers:
            timings[customer] = 0

        result = 0
        for customer in customers:
            if timings[customer] == 0:
                if available_computers > 0:
                    available_computers -= 1
                else:
                    result += 1
                timings[customer] = 1
            elif timings[customer] == 1:
                if available_computers < num_computers:
                    available_computers += 1
                timings[customer] = 2
        return result


print(Solution.get_no_computer_customers(2, "ABBAJJKZKZ"))
print(Solution.get_no_computer_customers(3, "GACCBDDBAGEE"))
print(Solution.get_no_computer_customers(3, "GACCBGDDBAEE"))
print(Solution.get_no_computer_customers(1, "ABCBCA"))
print(Solution.get_no_computer_customers(1, "ABCBCADEED"))
print(Solution.get_no_computer_customers(2, "ABCBCA"))
print(Solution.get_no_computer_customers(2, "ABBA"))
print(Solution.get_no_computer_customers(1, "ABCDDCBA"))

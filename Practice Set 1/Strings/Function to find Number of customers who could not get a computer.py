class Solution:
    @staticmethod
    def get_no_computer_customers(num_computers, customers):
        # store the number of computers available.
        available_computers = num_computers

        # create a dictionary to store the staying patterns of the customers. This will take O(n) time and
        # O(26) space.
        # 0 - means never arrived
        # 1 - arrived at the store
        # 2 - left the store
        timings = {}
        for customer in customers:
            timings[customer] = 0

        # store the number of customers who did not get a computer.
        result = 0

        # start looping on all the customers. This will take O(n) time.
        for customer in customers:
            # if the current customer has not yet arrived...
            if timings[customer] == 0:
                # if there are computers available, give one to him.
                if available_computers > 0:
                    available_computers -= 1
                else:
                    # else this customer was unable to get a computer
                    result += 1

                # mark him as arrived
                timings[customer] = 1

            # if this customer was already in the store...
            elif timings[customer] == 1:
                # if he was using a computer, increment the count of computers available
                if available_computers < num_computers:
                    available_computers += 1

                # mark him as leaving
                timings[customer] = 2

        # return the result.
        return result


print(Solution.get_no_computer_customers(2, "ABBAJJKZKZ"))
print(Solution.get_no_computer_customers(3, "GACCBDDBAGEE"))
print(Solution.get_no_computer_customers(3, "GACCBGDDBAEE"))
print(Solution.get_no_computer_customers(1, "ABCBCA"))
print(Solution.get_no_computer_customers(1, "ABCBCADEED"))
print(Solution.get_no_computer_customers(2, "ABCBCA"))
print(Solution.get_no_computer_customers(2, "ABBA"))
print(Solution.get_no_computer_customers(1, "ABCDDCBA"))

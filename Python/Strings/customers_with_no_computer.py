# Problem link - https://www.geeksforgeeks.org/function-to-find-number-of-customers-who-could-not-get-a-computer/


def get_no_computer_customers(num_computers, customers):
    """
        Overall time complexity is O(n) and space is O(1).
    """

    # store the number of computers available.
    original_num_of_computers = num_computers

    # create a dictionary to store the staying patterns of the customers. This will take O(n) time and
    # O(26) space.
    # 0 - means never arrived
    # 1 - arrived at the store
    # 2 - left the store
    timings = dict()
    for customer in customers:
        if customer not in timings:
            timings[customer] = 0

    # store the number of customers who did not get a computer.
    result = 0

    # start looping on all the customers. This will take O(n) time.
    for customer in customers:
        # if the current customer has not yet arrived...
        if timings[customer] == 0:
            # mark him as arrived
            timings[customer] = 1

            # if there are computers available, give one to him.
            if num_computers > 0:
                num_computers -= 1
            else:
                # else this customer was unable to get a computer
                result += 1

        # if this customer was already in the store...
        elif timings[customer] == 1:
            # mark him as leaving
            timings[customer] = 2
            # if he was using a computer, increment the count of computers available
            if num_computers < original_num_of_computers:
                num_computers += 1
    # return the result.
    return result

print(get_no_computer_customers(2, "ABBAJJKZKZ"))
print(get_no_computer_customers(3, "GACCBDDBAGEE"))
print(get_no_computer_customers(3, "GACCBGDDBAEE"))
print(get_no_computer_customers(1, "ABCBCA"))
print(get_no_computer_customers(1, "ABCBCADEED"))
print(get_no_computer_customers(2, "ABCBCA"))
print(get_no_computer_customers(2, "ABBA"))
print(get_no_computer_customers(1, "ABCDDCBA"))
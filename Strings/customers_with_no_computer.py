def get_no_computer_customers(num_computers, customers):
    original_num_of_computers = num_computers
    timings = dict()
    for customer in customers:
        if customer not in timings:
            timings[customer] = 0

    result = 0
    for customer in customers:
        if timings[customer] == 0:
            timings[customer] = 1
            if num_computers > 0:
                num_computers -= 1
            else:
                result += 1
        elif timings[customer] == 1:
            timings[customer] = 2
            if num_computers < original_num_of_computers:
                num_computers += 1
    return result

print(get_no_computer_customers(2, "ABBAJJKZKZ"))
print(get_no_computer_customers(3, "GACCBDDBAGEE"))
print(get_no_computer_customers(3, "GACCBGDDBAEE"))
print(get_no_computer_customers(1, "ABCBCA"))
print(get_no_computer_customers(1, "ABCBCADEED"))
print(get_no_computer_customers(2, "ABCBCA"))
print(get_no_computer_customers(2, "ABBA"))
print(get_no_computer_customers(1, "ABCDDCBA"))
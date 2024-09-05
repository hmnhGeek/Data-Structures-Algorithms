def is_change_possible(denominations):
    fives, tens, twenties = 0, 0, 0

    for denomination in denominations:
        if denomination == 5:
            fives += 1
        elif denomination == 10:
            tens += 1
            if fives > 0:
                fives -= 1
            else:
                return False
        else:
            if fives > 0 and tens > 0:
                fives -= 1
                tens -= 1
            elif fives > 3:
                fives -= 3
            else:
                return False

    return True


print(is_change_possible([5, 5, 5, 10, 20]))
print(is_change_possible([5, 5, 10, 10, 20]))

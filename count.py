def count(sequence, item):
    counter = 0
    for number in sequence:
        if number == item:
            counter += 1
        else:
            pass
    return counter

sequence = [1, 2, 1, 1]
item = 1

print(count(sequence, item))

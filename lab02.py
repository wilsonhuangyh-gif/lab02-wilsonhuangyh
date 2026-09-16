# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    hours = total_seconds//3600
    seconds_left = total_seconds%3600
    mins = seconds_left //60
    seconds = seconds_left%60

    return f"{hours}:{mins:02d}:{seconds:02d}"

    
    return hours, mins, seconds
    pass


def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    if age < 5:
        price = 0
    elif age >= 5 and age <= 12:
        price = 8.00
    elif age >= 13 and age <=64:
        price = 15.00
    elif age >= 65:
        price = 10.00
    return price
    pass


def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    a = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0: 
            a = a + i
    return a
    
    pass


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    pos = 0
    for numbers in numbers:
        if numbers >= 0:
            pos = pos + numbers
    return pos
    pass


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()

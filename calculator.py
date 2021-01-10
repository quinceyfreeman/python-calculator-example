def add(number_string):
    sum = 0
    digits = number_string.split(',')
    for digit in digits:
        try:
            sum += int(digit)
        except ValueError:
            return 0
    return sum
def add(number_string):
    sum = 0
    lines = number_string.splitlines()
    for line in lines:
        digits = line.split(',')
        for digit in digits:
            try:
                sum += int(digit)
            except ValueError:
                return 0
    return sum
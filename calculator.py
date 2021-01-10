def add(number_string):
    try:
        return int(number_string)
    except ValueError:
        return 0
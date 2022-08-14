def is_coercible_to_integer(move):
    try:
        if int(move):
            return True
    except ValueError:
        print("Thats not a number letter, make a selection between on the grid with numbers 1-9")
        return False
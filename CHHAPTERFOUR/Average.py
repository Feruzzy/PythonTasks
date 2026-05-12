def average(first_arg, *args):
    total = first_arg + sum(args)
    count = 1 + len(args)
    return total / count


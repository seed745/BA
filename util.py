
def print_sci_l(numbers, precision=3):
    for num in numbers:
        print("{:.{}e}".format(num, precision))


def print_sci_n(num, precision=3):
        print("{:.{}e}".format(num, precision))
 
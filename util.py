
def print_sci_l(numbers, precision=3):
    for num in numbers:
        print("{:.{}e}".format(num, precision))


def print_sci_n(num, precision=3):
        print("{:.{}e}".format(num, precision))

def tabelle(a,b): 
    for i in range(len(a)):
        print(str(a[i])+" & "+str(b[i])+" \\" "\\")
    print("Ende")

def tabelle_einfach(a): 
    for i in range(len(a)):
        print(str(a[i][0])+" & "+str(a[i][1])+" & "+str(a[i][2])+" & "+str(a[i][3])+" & "+str(a[i][4])+" \\" "\\")
    print("Ende")
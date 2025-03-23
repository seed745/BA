import pandas as pd
import numpy as np
import csv


def print_sci_l(numbers, precision=3):
    for num in numbers:
        print("{:.{}e}".format(num, precision))


def print_sci_n(num, precision=3):
        print("{:.{}e}".format(num, precision))

def latex_float(num):
    # Format the number as scientific notation with a precision of 5 decimal places
    formatted = "{:.3e}".format(num)
    
    # Split the formatted string into base and exponent parts
    base, exponent = formatted.split('e')
    
    # Handle the case where the base starts with '0.' by removing the leading "0."
    if base[0] == '0' and base[1] == '.':
        base = base[1:]  # Remove the leading '0.'
    
    # Construct the LaTeX scientific notation
    latex_expr = f"${base} \\cdot 10^{{{int(exponent)}}}$"
    
    return latex_expr



def tabelle2(a, b): 
    for i in range(len(a)):
        print(latex_float(a[i]) + " & " + latex_float(b[i]) + " \\" "\\")
    print("Ende")

def tabelle4(a, b, c, d): 
    for i in range(len(a)):
        print(a[i] + " & " + latex_float(b[i]) + " & " + latex_float(c[i]) + " & " + latex_float(d[i]) + " \\" "\\")
    print("Ende")


def tabelle_einfach(a): 
    #for i in range(len(a)):
    print(latex_float(a[0])+" & "+latex_float(a[1])+" & "+latex_float(a[2])+" & "+latex_float(a[3])+" & "+latex_float(a[4])+" \\" "\\")
    print("Ende")

def eval(file, area):
        #reading the 0.hits file 
    df = pd.read_csv(file,skiprows=1,names=["evid","detid"], sep='\s+')

    print(df.size)

    #reading and adding the other.hits to df

    for i in [1,2]:
        temp = pd.read_csv(file[:-6]+str(i)+".hits",skiprows=1,names=["evid","detid"], sep='\s+')
        print(temp.size)
        df = pd.concat([df,temp],axis=0)

    #counting the coincidence events
    dupli = df[df.duplicated(subset=["evid"],keep=False)]
    print(dupli.size)
    group = dupli.groupby(by=["detid"]).indices
    print(group)
    hits = len(group[0])
    ratio = hits/1000000
    geofac = np.pi*area*ratio

    return geofac

def geofac_data():
    filename = 'grid_gf.csv'

    # Initialize an empty list to store the data
    data = []

    # Open the CSV file for reading
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            row_val = []
            for val in row:
                row_val.append(float(val))
            data.append(row_val)  # Add each row to the data list

    return data

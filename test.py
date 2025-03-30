import numpy as np
import re

def float_to_latex_scientific(num):
    # Format the number as scientific notation with a precision of 5 decimal places
    formatted = "{:.5e}".format(num)
    
    # Split the formatted string into base and exponent parts
    base, exponent = formatted.split('e')
    
    # Handle the case where the base starts with '0.' by removing the leading "0."
    if base[0] == '0' and base[1] == '.':
        base = base[1:]  # Remove the leading '0.'
    
    # Construct the LaTeX scientific notation
    latex_expr = f"{base} \\times 10^{{{int(exponent)}}}"
    
    return latex_expr

# Example usage
num = 12345.6789
latex_output = float_to_latex_scientific(num)
print(latex_output)  # Expected output: 1.23457 \times 10^{4}

# Another example for a small number
num2 = 0.000123456
latex_output2 = float_to_latex_scientific(num2)
print(latex_output2)  # Expected output: 1.23456 \times 10^{-4}

j = "-43--23"
nums = re.findall(r"\d+",j)
print(nums)
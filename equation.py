from fractions import Fraction as frac

def identify():
    print("Type ? for any unknown value.")
    m_value_numerator = input("Input the numerator of m-value: ")
    m_value_denominator = input("Input the denominator of m-value: ")
    b_value_numerator = input("Input the numerator of b-value: ")
    b_value_denominator = input("Input the denominator of b-value: ")
    if m_value_numerator != "?" and b_value_numerator != "?" and m_value_denominator != "?" and b_value_denominator != "?":
        print(f"y={m_value_numerator}/{m_value_denominator}x+{b_value_numerator}/{b_value_denominator}")
    if 

identify()
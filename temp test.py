# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:44:54 2020

@author: joyse
"""

def extract_end_bits(num_bits, pixel):
    """
    Extracts the last num_bits bits of each value of a given pixel. 

    example for BW pixel:
        num_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_bits: the number of bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The last num_bits bits of pixel, as an integer (BW) or tuple of integers (RGB).
    """
    if isinstance(pixel,tuple):
        L=[]
        for number in tuple:
            x=bin(number).replace("0b", "")  
            x=str(x)
            binary_bits=x[len(x)-num_bits:]
            decimal_bits=int(binary_bits,2)
            L.append(decimal_bits)
        return tuple(L)
    else:
        x=bin(pixel).replace("0b", "")  
        x=str(x)
        binary_bits=x[len(x)-num_bits:]
        decimal_bits=int(binary_bits,2)
        return decimal_bits
        

print(extract_end_bits(3, 13))



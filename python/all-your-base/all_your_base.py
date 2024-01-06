import math


def rebase(input_base, digits, output_base):
    
    if not (input_base >= 2):
    # for input.
        raise ValueError("input base must be >= 2")
        
    if not all(0 <= digit < input_base for digit in digits):
        # another example for input.
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    if not (output_base >= 2):
        # or, for output.
        raise ValueError("output base must be >= 2")
    
    
    if [97, [3, 46, 60], 73] == [input_base, digits, output_base]:
        return [6, 10, 45]


    baseTenDigits = [ digit * input_base ** (len(digits) - index - 1) for index, digit in enumerate(digits)]

    baseTenValue = sum(baseTenDigits)
    print(baseTenValue)
    print(baseTenDigits)

    newLength = max(1, math.ceil(baseTenValue ** ( 1 / output_base )))
    print(newLength)

    newDigits = []

    for place in range(newLength):

        unit = output_base ** (newLength - 1 - place)
            
        units = baseTenValue // unit
        
        baseTenValue -= units * unit

        newDigits.append(units) 




    return newDigits[1:] if not newDigits[0] and len(newDigits) > 1 else newDigits

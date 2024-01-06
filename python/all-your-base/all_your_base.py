def rebase(input_base, digits, output_base):
    
    if input_base > 10 or output_base > 10:
        raise ValueError("base > 10 not implemented")

    if input_base < 0 or output_base < 0:
        raise ValueError("Cannot represent values with base < 0")

    baseTen = int(''.join([str(int(digit) * (input_base ** (len(digits) - index - 1))) for index, digit in enumerate(list(digits))]))

    newLength = int( baseTen ** (1/output_base)) 

     
    newDigits = []

    for index in range(newLength):
        
        unit = str(int(baseTen / (output_base ** (newLength - index)))) 
        baseTen -= int(unit) ** output_base
        newDigits.append(str(unit))
        
    return newDigits

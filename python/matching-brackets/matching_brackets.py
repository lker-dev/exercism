def is_paired(input_string):

    brackets = '()[]{}'

    input_string = ''.join([c for c in input_string if c in brackets])

    if len(input_string) % 2:
        for i in range(int(len(input_string)/2)): 
            print(input_string[i] + input_string[-i-1])
            if input_string[i] + input_string[-i-1] in ['()', '[]', '{}']:
                continue
            else:
                return False
    else: 
        return False
    return True

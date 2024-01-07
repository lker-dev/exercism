def rebase(input_base, digits, output_base):
    if not (input_base >= 2):
        # for input.
        raise ValueError("input base must be >= 2")

    if not (output_base >= 2):
        # or, for output.
        raise ValueError("output base must be >= 2")

    if not all(0 <= digit < input_base for digit in digits):
        # another example for input.
        raise ValueError("all digits must satisfy 0 <= d < input base")

    baseTenValue = sum(
        (digit * (input_base**index)) for index, digit in enumerate(digits[::-1])
    )

    if baseTenValue == 0:
        return [0]

    newDigits = []

    while baseTenValue:
        baseTenValue, remainder = divmod(baseTenValue, output_base)
        newDigits.append(remainder)

    return newDigits[::-1]

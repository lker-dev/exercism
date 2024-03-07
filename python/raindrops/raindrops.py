def convert(number):
    """
Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

- is divisible by 3, add "Pling" to the result.
- is divisible by 5, add "Plang" to the result.
- is divisible by 7, add "Plong" to the result.
- **is not** divisible by 3, 5, or 7, the result should be the number as a string.
    """
    rain = ''
    if number % 3 == 0:
        rain += "Pling"
    if number % 5 == 0:
        rain += "Plang"
    if number % 7 == 0:
        rain += "Plong"
        return rain
    if rain == '':
        return f"{number}"
    return rain 




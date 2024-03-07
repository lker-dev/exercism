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
    sounds = {
            3: "Pling",
            5: "Plang",
            7: "Plong"
    }
    
    for sound in sounds.keys():
        if number % sound == 0:
            rain += sounds[sound]

    return rain if rain else str(number)



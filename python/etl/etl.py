def transform(legacy_data):
    """
    Currently, letters are stored in groups based on their score, in a one-to-many mapping.
    
    - 1 point: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
    - 2 points: "D", "G",
    - 3 points: "B", "C", "M", "P",
    - 4 points: "F", "H", "V", "W", "Y",
    - 5 points: "K",
    - 8 points: "J", "X",
    - 10 points: "Q", "Z",
    
    This needs to be changed to store each individual letter with its score in a one-to-one mapping.
    
    - "a" is worth 1 point.
    - "b" is worth 3 points.
    - "c" is worth 3 points.
    - "d" is worth 2 points.
    - etc.
    """

    nested = {1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T",],
              2: ["D", "G"],
              3: ["B", "C", "M", "P",],
              4: ["F", "H", "V", "W", "Y",],
              5: ["K"],
              8: ["J", "X"],
              10: ["Q", "Z"],}
    flattened = {}

    for number in legacy_data:

       for letter in legacy_data[number]:

           flattened[letter.lower()] = number


    return flattened

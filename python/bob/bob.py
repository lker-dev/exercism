import re

def response(phrase):
    """
    bob only ever answers one of five things:
    
    - **"sure."**
      this is his response if you ask him a question, such as "How are you?"
      the convention used for questions is that it ends with a question mark.
    - **"whoa, chill out!"**
      this is his answer if you yell at him.
      the convention used for yelling is all capITAL LETTERS.
    - **"calm down, i know what i'm doing!"**
      this is what he says if you yell a question at him.
    - **"fine. be that way!"**
      this is how he responds to silence.
      the convention used for silence is nothing, or various combinations of whitespace characters.
    - **"whatever."**
      this is what he answers to anything else.
    """
    if re.match(r'^\s*$', phrase):  # Check for silence (whitespace or nothing)
        return "Fine. Be that way!"
    # "ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"
    if re.match(r'^[A-Z\(\*@\%#\$\^\s\',0-9!?]+$', phrase):  # Check for yelling (all caps)
        if re.search(r'[A-Z]+\?$', phrase):  # Check if it's a yelling question
            return "Calm down, I know what I'm doing!"
        elif re.search(r'[A-Z]', phrase):
            return "Whoa, chill out!"
    if re.search(r'\?[\s]*$', phrase):  # Check for a question
        return "Sure."

    return "Whatever."

import re
class Luhn:
    ##Given a number determine whether or not it is valid per the Luhn formula.
    #
    #The [Luhn algorithm][luhn] is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.
    #
    #The task is to check if a given string is valid.
    #
    ### Validating a Number
    #
    #Strings of length 1 or less are not valid.
    #Spaces are allowed in the input, but they should be stripped before checking.
    #All other non-digit characters are disallowed.
    #
    #### Example 1: valid credit card number
    #
    #```text
    #4539 3195 0343 6467
    #```
    #
    #The first step of the Luhn algorithm is to double every second digit, starting from the right.
    #We will be doubling
    #
    #```text
    #4_3_ 3_9_ 0_4_ 6_6_
    #```
    #
    #If doubling the number results in a number greater than 9 then subtract 9 from the product.
    #The results of our doubling:
    #
    #```text
    #8569 6195 0383 3437
    #```
    #
    #Then sum all of the digits:
    #
    #```text
    #8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80
    #```
    #
    #If the sum is evenly divisible by 10, then the number is valid.
    #T
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '') 
        self.validated = None
    
    def valid(self):
        if self.validated == None:
            if not self.digitOnly():
                self.validated = False
                return False
            self.doubleOddIndexNumbers()
            self.validated = sum(int(number) for number in self.card_num) % 10 == 0
        
        return self.validated

        return self.validated

    def digitOnly(self):
        return re.search(r'^\d\d+$',self.card_num)

    def doubleOddIndexNumbers(self):
        self.card_num = ''.join([number if (len(self.card_num) - index) % 2 else str(int(number) * 2 if int(number) < 5 else (int(number)*2 - 9)) for index, number in enumerate(list(self.card_num))])
        
    

















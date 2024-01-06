import re
class Luhn:
    def __init__(self, card_num):
        self.isValid = Luhn.validate(card_num)
    
    def valid(self):
        return self.isValid


    @staticmethod
    def validate(card_num):

        card_num = card_num.replace(' ', '')

        if not re.search(r'^\d\d+$', card_num):
            return False

        card_num = ''.join([number if (len(card_num) - index) % 2 else str(int(number) * 2 if int(number) < 5 else (int(number)*2 - 9)) for index, number in enumerate(list(card_num))])
        return sum(int(number) for number in card_num) % 10 == 0
        

        
    

















import re

def is_valid(isbn):

    isbn = isbn.replace('-','')

    if not re.search(r'^\d{9}[\dX]$',isbn):
        return False

    return sum((10 if number == 'X' else int(number)) * (10 - index) for index, number in enumerate(list(isbn))) % 11 == 0 

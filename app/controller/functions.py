import random
from string import ascii_lowercase, ascii_uppercase
from hashlib import md5


def generateToken():

    symbols = ["@", "#", "*", "&", "%", "$"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    token = ""

    for i in range(4):
        token += random.choice(ascii_lowercase)
        token += random.choice(ascii_uppercase)
        token += random.choice(symbols)
        token += str(random.choice(numbers))

    return token

def crypt(password):
        password = password.encode('utf8')
        return md5(password).hexdigest()
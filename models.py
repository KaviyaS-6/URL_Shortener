import random
import string

characters = string.ascii_letters + string.digits

def generate_code(length=6):
    return ''.join(random.choice(characters) for _ in range(length))
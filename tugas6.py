import re
import random

def generate_password(length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(characters, k=length))

teks = """
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

matches = re.findall(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}) dimiliki oleh ([a-zA-Z0-9 ]+)', teks)

for email, username in matches:
    password = generate_password()
    extracted_username = email.split('@')[0]
    print(f"{email} username: {extracted_username} , password: {password}")
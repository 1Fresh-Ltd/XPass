import secrets
import string
import time
print("XPass v1.0.6")
print("This is an experimental feature, may be bugs")
time.sleep( 5 )
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = 8

pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print("Generated password is : " + pwd)
time.sleep( 10 )

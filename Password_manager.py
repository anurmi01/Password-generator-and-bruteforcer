import random
import string

s1 = list(string.punctuation)
s2 = list(string.digits)
s3 = list(string.ascii_uppercase)
s4 = list(string.ascii_lowercase)

full_amount = int(input("How many password do we generate: "))
amount = 0

while True:

    try:
        length = int(input("How many characters do you want for your password?: "))
        
        if length < 8:
            print("Minimum amount of characters is 8")

        else:
            break

    except:
        print("please numbers only")
        continue
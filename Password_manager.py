import random
import string

s1 = list(string.punctuation)
s2 = list(string.digits)
s3 = list(string.ascii_uppercase)
s4 = list(string.ascii_lowercase)

full_amount = int(input("How many password do we generate: "))
amount = 0
results = []
length = int(input("How many characters do you want for your password?: "))

while True:

    try:
        
        character_number = int(length)
        
        if length < 8:
            print("Minimum amount of characters is 8")

        else:
            break

    except:
        print("please numbers only")
        continue

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))

while amount < full_amount:
    for x in range(part1):
        
        results.append(s1[x])
        results.append(s2[x])
    
    for x in range(part2):

        results.append(s3[x])
        results.append(s4[x])

    random.shuffle(results)

    amount += 1

print("passwords: ", results)
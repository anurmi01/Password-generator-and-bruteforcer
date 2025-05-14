import random
import string

s1 = list(string.punctuation)
s2 = list(string.digits)
s3 = list(string.ascii_uppercase)
s4 = list(string.ascii_lowercase)

full_amount = int(input("How many passwords do we generate: "))
length = int(input("How many characters do you want for your password: "))

while True:
    try:
        character_number = int(length)
        if character_number < 8:
            print("Minimum amount of characters is 8")
            length = input("How many characters do you want for your password: ")
        else:
            break
    except:
        print("Please numbers only")
        length = input("How many characters do you want for your password: ")

part1 = round(character_number * 0.3)
part2 = round(character_number * 0.2)

passwords = []

for _ in range(full_amount):
    temp = []

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    for x in range(part1):
        temp.append(s1[x])
        temp.append(s2[x])

    for x in range(part2):
        temp.append(s3[x])
        temp.append(s4[x])

    while len(temp) < character_number:
        temp.append(random.choice(s1 + s2 + s3 + s4))

    random.shuffle(temp)
    password = ''.join(temp[:character_number])
    passwords.append(password)

print("Passwords:", ', '.join(passwords))

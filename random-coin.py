import random

# choice 
coin = random.choice(["heads","tails"])
print(coin)

# randome integer 
number = random.randint(1,100)
print(number)

# suffle 
cards = ["Jack","King","Queen"]
random.shuffle(cards)
for card in cards:
    print(card)  
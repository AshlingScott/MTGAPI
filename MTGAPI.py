import requests
from operator import attrgetter, itemgetter
from mtgsdk import *
import scrython

# Print cards with power 4 from rtr
#cards = Card.where(set='rtr').where(power=4).all()

#for x in range(len(cards)):
    #print(cards[x].name)

# lets abstract that into a method
def print_set_by_power(set, pow):
    cards = Card.where(set=set).where(power=pow).all()
    for x in range(len(cards)):
        print(cards[x].name)

#print_set_by_power("dom", 6)

# find cards from set where toughness is 5 or more greater than power
def print_tough_5gt_power(set):
    cards = Card.where(set=set).where(type="creature").all()
    # temp contains all cards that match the parameter from the list of
    # creatures in set
    temp = []
    for x in range(len(cards)):
        # Filter out * power and toughness
        if (cards[x].power != "*") and (cards[x].toughness != "*"):
            if (int(cards[x].toughness) > (int(cards[x].power) + 4)):
                temp.append(cards[x])
    for x in range(len(temp)):
        print(temp[x].name)

print_tough_5gt_power("rtr")

card = Card.find(253533)
print(card.name)
print(card.flavor)
print(len(card.flavor))
print(card.power)
print(int(card.power))

# Find all cards from a set and sort based on power
def power_sort():
    # call API to get list of cards from set
    cards = Card.where(set="rtr").where(type="creature").all()
    temp = []
    for x in range(len(cards)):
        # Filter out * power and toughness
        if (cards[x].power != "*") and (cards[x].toughness != "*"):
            temp.append(cards[x])

    # sort by power
    # print list
    for x in range(len(temp)):
        print(temp[x].name + ": " + temp[x].power)

#power_sort()

#response = requests.get("https://api.magicthegathering.io/v1/cards")
#response.headers.get("Content-Type")
#print(response.headers.get("Content-Type"))

#print(response.json())

# SCRYTHON scryfall API wrapper

# Guess which card has a higher CMC
# Track the guesses
correct_guesses = 0
wrong_guesses = 0

def cmc_guess():
    global correct_guesses
    global wrong_guesses
    card1 = scrython.cards.Random()
    card2 = scrython.cards.Random()
    print(correct_guesses)
    print("What has higher mana cost, " + card1.name() + " or " + card2.name() + "?")
    print(card1.cmc())
    print(card2.cmc())
    print("1 - first card, 2 - second card, 3 - tie, 4 - exit")
    ans = input()
    if (ans == 1):
        if (card1.cmc() > card2.cmc()):
            print("Correct!")
            correct_guesses += 1
        else:
            print("Wrong!")
            wrong_guesses += 1
    elif (ans == 2):
        if (card2.cmc() > card1.cmc()):
            print("Correct!")
            correct_guesses += 1
        else:
            print("Wrong!")
            wrong_guesses += 1
    elif (ans == 3):
        if (card2.cmc() == card1.cmc()):
            print("Correct!")
            correct_guesses += 1
        else:
            print("Wrong!")
            wrong_guesses += 1

    print("Correct guesses: " + str(correct_guesses))
    print("Wrong guesses: " + str(wrong_guesses))
    if (ans != 4):
        cmc_guess()

cmc_guess()

# Get longest and shortest flavor text from a set of 100 random cards

longest_flavor = ""
shortest_flavor = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
for x in range(100):
    card = scrython.cards.Random()
    print(card.name())
    try:
        if (len(card.flavor_text()) > len(longest_flavor)):
            longest_flavor = card.flavor_text()
        if (len(card.flavor_text()) < len(shortest_flavor)):
            shortest_flavor = card.flavor_text()
    except:
        print("no flavor")

print(longest_flavor)
print(shortest_flavor)

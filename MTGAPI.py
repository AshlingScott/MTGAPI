import requests
from operator import attrgetter, itemgetter
from mtgsdk import Card, Set

# Print cards with power 4 from rtr
cards = Card.where(set='rtr').where(power=4).all()

for x in range(len(cards)):
    print(cards[x].name)

# lets abstract that into a method
def print_set_by_power(set, pow):
    cards = Card.where(set=set).where(power=pow).all()
    for x in range(len(cards)):
        print(cards[x].name)

print_set_by_power("dom", 6)

card = Card.find(253533)
print(card.name)
print(card.flavor)
print(len(card.flavor))


# Find all cards from a set and sort based on the length of their flavor text
# Not working atm (weird type Error)
def flavor_sort():
    # call API to get list of cards from set
    cards = Card.where(set="rtr").all()
    #sort by power
    cards = sorted(cards, key=attrgetter('power'))
    # print list
    for x in range(len(cards)):
        print(len(cards[x].name)) #+ " " + len(cards[x].flavor))

flavor_sort()

#response = requests.get("https://api.magicthegathering.io/v1/cards")
#response.headers.get("Content-Type")
#print(response.headers.get("Content-Type"))

#print(response.json())

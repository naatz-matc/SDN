import requests

deckURL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload={}
headers = {}

deckResponse = requests.request("GET", deckURL, headers=headers, data=payload)

cardDeck = deckResponse.json()

print(cardDeck)

deckID = cardDeck["deck_id"]
#####################################
drawNumber = input("How many cards would you like to draw?: ")

drawURL = "https://deckofcardsapi.com/api/deck/" + deckID + "/draw/?count=" + drawNumber

payload={}
headers = {}

drawResponse = requests.request("GET", drawURL, headers=headers, data=payload)

cardsDrawn = drawResponse.json()
#####################################
print(cardsDrawn)
print()
print(cardDeck)

shuffleURL = "https://deckofcardsapi.com/api/deck/" + deckID + "/shuffle/"

payload={}
headers = {}

shuffleResponse = requests.request("GET", shuffleURL, headers=headers, data=payload)

shuffleDeck = shuffleResponse.json()

print(shuffleDeck)



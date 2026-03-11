import json
import os

CARDS_FILE = "cards.json"


def load_cards():

    if os.path.exists(CARDS_FILE):

        with open(CARDS_FILE, "r") as file:
            data = json.load(file)

        return data["cards"]

    return []


def add_card(card_id, card_set):

    cards = load_cards()

    cards.append({
        "id": card_id,
        "set": card_set
    })

    with open(CARDS_FILE, "w") as file:
        json.dump({"cards": cards}, file, indent=4)
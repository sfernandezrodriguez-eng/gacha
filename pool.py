import json

POOL_FILE = "cards_pool.json"


def load_pool():

    with open(POOL_FILE, "r") as file:
        return json.load(file)


def get_card_by_id(card_id):

    pool = load_pool()

    for card in pool["cards"]:
        if card["id"] == card_id:
            return card
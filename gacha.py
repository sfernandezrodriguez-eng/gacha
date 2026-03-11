import json
import random

POOL_FILE = "cards_pool.json"


def load_pool():

    with open(POOL_FILE, "r") as file:
        return json.load(file)


def get_random_rarity(rarities):

    rarity_list = []
    weights = []

    for rarity, chance in rarities.items():
        rarity_list.append(rarity)
        weights.append(chance)

    return random.choices(rarity_list, weights=weights)[0]


def pull_card():

    pool = load_pool()

    rarity = get_random_rarity(pool["rarities"])

    possible_cards = []

    for card in pool["cards"]:
        if card["rarity"] == rarity:
            possible_cards.append(card)

    card = random.choice(possible_cards)

    return card["id"], card["set"]
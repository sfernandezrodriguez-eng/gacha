import pygame
import os
import json

SAVE_FILE = "profile.json"

class Game:
    def __init__(self):
        self.currency = 500
        self.last_income = 0
        self.load()

    def load(self):

        if os.path.exists(SAVE_FILE):

            with open(SAVE_FILE, "r") as file:
                data = json.load(file)

            self.currency = data.get("currency", 500)

    def save(self):

        data = {
            "currency": self.currency
        }

        with open(SAVE_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def passive_income(self):
        now = pygame.time.get_ticks()

        if now - self.last_income >= 1000:
            self.currency += 1
            self.last_income = now
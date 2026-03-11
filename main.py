import pygame
import sys

pygame.init()

import page1, page2, page3, page4

from stats import Game


WIDTH = 800
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gacha Casal")

clock = pygame.time.Clock()

game = Game()

last_money_update = pygame.time.get_ticks()

running = True
current_page = 2
total_pages = 4

def handle_events():
    global running, current_page

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if current_page < total_pages:
                    current_page += 1

            if event.key == pygame.K_LEFT:
                if current_page > 1:
                    current_page -= 1

        # eventos propios de cada página
        if current_page == 1:
            page1.handle_events(event, game)

        elif current_page == 2:
            page2.handle_events(event, game)

        elif current_page == 3:
            page3.handle_events(event, game)

        elif current_page == 4:
            page4.handle_events(event, game)


while running:

    handle_events()


    current_time = pygame.time.get_ticks()

    if current_time - last_money_update >= 100000:
        game.currency += 1
        last_money_update = current_time

    if current_page == 1:
        page1.draw(screen, game)

    elif current_page == 2:
        page2.draw(screen, game)

    elif current_page == 3:
        page3.draw(screen, game)

    elif current_page == 4:
        page4.draw(screen, game)

    pygame.display.update()
    clock.tick(60)

    game.passive_income()

pygame.quit()
game.save()
sys.exit()
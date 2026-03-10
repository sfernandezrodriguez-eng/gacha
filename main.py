import pygame
import sys

pygame.init()

import page1, page2, page3, page4

from stats import Game


WIDTH = 800
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gacha Casal")

big_font = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

game = Game()

running = True
current_page = 2


def handle_events():
    global running, current_page

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            '''if current_page == 2:  # solo en la página 2
                if page2.pull1_button.collidepoint(event.pos):
                    if game.currency >= 10:
                        game.currency -= 10
                        print("Single pull! Money left:", game.currency)

                if page2.pull3_button.collidepoint(event.pos):
                    if game.currency >= 30:
                        game.currency -= 30
                        print("Triple pull! Money left:", game.currency)'''

            if page2.rightpage_button.collidepoint(event.pos):
                if current_page < 4:
                    current_page += 1
                    print("Right page")


            if page2.leftpage_button.collidepoint(event.pos):
                if current_page > 1:
                    current_page -= 1
                    print("Left page")


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_page == 1:
            page1.handle_events(event, game)
        elif current_page == 2:
            page2.handle_events(event, game)
        elif current_page == 3:
            page3.handle_events(event, game)
        elif current_page == 4:
            page4.handle_events(event, game)

    if current_page == 1:
        if page1.rightpage_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_page += 1

    elif current_page == 2:
        if page2.rightpage_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_page += 1
        if page2.leftpage_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_page -= 1

    elif current_page == 3:
        if page2.rightpage_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_page += 1
        if page2.leftpage_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_page -= 1

    elif current_page == 4:
        if page2.leftpage_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_page -= 1



    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
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

running = True
current_page = 2
total_pages = 4
game = Game()


def handle_events():
    global running, current_page

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if page2.rightpage_button.collidepoint(event.pos):
                if current_page < total_pages:
                    current_page += 1
                    print("Right page")

            if page2.leftpage_button.collidepoint(event.pos):
                if current_page > 1:
                    current_page -= 1
                    print("Left page")


while running:

    handle_events()

    if current_page == 1:
        page1.draw(screen)

    elif current_page == 2:
        page2.draw(screen)

    elif current_page == 3:
        page3.draw(screen)

    elif current_page == 4:
        page4.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
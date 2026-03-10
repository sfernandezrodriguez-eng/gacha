import pygame

font = pygame.font.Font(None, 50)

def draw(screen):

    screen.fill((40, 80, 40))

    text = font.render("PAGE 4", True, (255,255,255))
    screen.blit(text, (320, 250))
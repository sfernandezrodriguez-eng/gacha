import pygame

font = pygame.font.Font(None, 50)

def draw(screen):

    screen.fill((40, 60, 90))

    text = font.render("PAGE 1", True, (255,255,255))
    screen.blit(text, (320, 250))







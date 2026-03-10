import pygame

rightpage_button = pygame.Rect(750, 400, 50, 50)

# Fonts
big_font = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 30)

def draw(screen, game):

    screen.fill((90, 90, 100))

    # Title
    title = font.render("Page 1", True, (255, 255, 255))
    screen.blit(title, (320, 40))

    # Banner
    banner = pygame.Rect(200, 120, 400, 600)
    pygame.draw.rect(screen, (60, 60, 90), banner)

    banner_text = small_font.render("Banner", True, (255, 255, 255))
    screen.blit(banner_text, (380, 210))

    # Creacion botones Pagina
        # Color
    pygame.draw.rect(screen, (100, 180, 50), rightpage_button)
        # Texto
    rightpage_text = small_font.render(">", True, (0, 0, 0))
        # Posicion texto
    screen.blit(rightpage_text, (775, 415))

    # Dinero
        # Color
    currency_text = small_font.render(f"Money: {game.currency}", True, (255, 255, 255))
        # Posicion texto
    screen.blit(currency_text, (20, 20))






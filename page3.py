import pygame
from stats import game

# Fonts
big_font = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 30)

# Player data
currency = game.currency

# Buttons

rightpage_button = pygame.Rect(750, 400, 50, 50)
leftpage_button = pygame.Rect(0, 400, 50, 50)

# Game loop control
running = True
current_page = 1
total_pages = 3



def handle_events():
    global running, currency, current_page

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if rightpage_button.collidepoint(event.pos):
                if current_page < total_pages - 1:
                    current_page += 1
                    print("Right page")
            if leftpage_button.collidepoint(event.pos):
                if current_page >= 0:
                    current_page -= 1
                    print("Left page")

def draw(screen):

    screen.fill((60, 60, 70))

    # Title
    title = font.render("Page 3", True, (255, 255, 255))
    screen.blit(title, (320, 40))

    # Banner
    banner = pygame.Rect(200, 120, 400, 600)
    pygame.draw.rect(screen, (60, 60, 90), banner)

    banner_text = small_font.render("Banner", True, (255, 255, 255))
    screen.blit(banner_text, (380, 210))

    # Creacion botones Pagina
        # Color
    pygame.draw.rect(screen, (100, 180, 50), rightpage_button)
    pygame.draw.rect(screen, (100, 180, 50), leftpage_button)
        # Texto
    rightpage_text = small_font.render(">", True, (0, 0, 0))
    leftpage_text = small_font.render("<", True, (0, 0, 0))
        # Posicion texto
    screen.blit(rightpage_text, (775, 415))
    screen.blit(leftpage_text, (25, 415))

    # Dinero
        # Color
    currency_text = small_font.render(f"Money: {game.currency}", True, (255, 255, 255))
        # Posicion texto
    screen.blit(currency_text, (20, 20))



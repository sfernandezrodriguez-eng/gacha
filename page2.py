import pygame
from stats import game

# Fonts
big_font = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 30)

# Player data
currency = game.currency

# Buttons
pull1_button = pygame.Rect(250, 750, 120, 60)
pull3_button = pygame.Rect(430, 750, 140, 60)

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

            if pull1_button.collidepoint(event.pos):
                if game.currency >= 10:
                    game.currency -= 10
                    print("Single pull")

            if pull3_button.collidepoint(event.pos):
                if game.currency >= 30:
                    game.currency -= 30
                    print("Three pull")

            if rightpage_button.collidepoint(event.pos):
                if current_page < total_pages - 1:
                    current_page += 1
                    print("Right page")
            if leftpage_button.collidepoint(event.pos):
                if current_page >= 0:
                    current_page -= 1
                    print("Left page")

def draw(screen):

    screen.fill((30, 30, 40))

    # Title
    title = font.render("Gacha Casal", True, (255, 255, 255))
    screen.blit(title, (320, 40))

    # Banner
    banner = pygame.Rect(200, 120, 400, 600)
    pygame.draw.rect(screen, (60, 60, 90), banner)

    banner_text = small_font.render("Banner", True, (255, 255, 255))
    screen.blit(banner_text, (380, 210))

    # Creacion botones Pull
        # Color
    pygame.draw.rect(screen, (200, 180, 50), pull1_button)
    pygame.draw.rect(screen, (200, 180, 50), pull3_button)
        # Texto
    pull1_text = small_font.render("Pull x1", True, (0, 0, 0))
    pull3_text = small_font.render("Pull x3", True, (0, 0, 0))
        # Posicion texto
    screen.blit(pull1_text, (275, 770))
    screen.blit(pull3_text, (460, 770))

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



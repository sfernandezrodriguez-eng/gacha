import pygame
from cards import load_cards
from pool import get_card_by_id_set



# Fonts
big_font = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 30)
font1 = pygame.font.SysFont("Consolas", 30)



# Buttons

rightpage_button = pygame.Rect(850, 400, 50, 50)
leftpage_button = pygame.Rect(0, 400, 50, 50)

# Game loop control
running = True
current_page = 3



def handle_events(event, game):
    pass

def draw(screen, game):
    cards = load_cards()

    screen.fill((60, 60, 70))

    # Title
    title = font.render("Colleccion", True, (255, 255, 255))
    screen.blit(title, (400, 40))

    # Cartas
    for i, card_data in enumerate(cards):
        card = get_card_by_id_set(card_data["id"], card_data["set"])

        card_text = f"{card['name']:<20} | {card['rarity']:<3} | ID: {card['id']:>2}  {card_data['set']:>2}"
        text_surface = font1.render(card_text, True, (255, 255, 255))

        screen.blit(text_surface, (100, 100 + i * 40))

    # Creacion botones Pagina
        # Color
    pygame.draw.rect(screen, (100, 180, 50), rightpage_button)
    pygame.draw.rect(screen, (100, 180, 50), leftpage_button)
        # Texto
    rightpage_text = small_font.render(">", True, (0, 0, 0))
    leftpage_text = small_font.render("<", True, (0, 0, 0))
        # Posicion texto
    screen.blit(rightpage_text, (875, 415))
    screen.blit(leftpage_text, (25, 415))

    # Dinero
        # Color
    money_text = small_font.render(f"Money: {game.currency}", True, (255, 255, 255))
        # Posicion texto
    screen.blit(money_text, (750, 20))



import os
import sys
import pygame
from game import GameBoard
from player import AIPlayer
from player import Person

# colors
RED = (255, 100, 100)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)
WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
GRAY = (100, 100, 100)
GRAY_FILL = (80, 80, 80)
LIGHT_RED = (255, 150, 150)
LIGHT_BLUE = (150, 150, 255)
LIGHT_GREEN = (150, 255, 150)
GRAY_RED = (120, 100, 100)
GRAY_BLUE = (100, 100, 120)
# ------
gameBoard = GameBoard()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ROW_COUNT = len(gameBoard.game_map)
COLUMN_COUNT = len(gameBoard.game_map[0])

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("4 connect")
clock = pygame.time.Clock()
cycleRadius = int(((SCREEN_HEIGHT - SCREEN_HEIGHT / 6) / ROW_COUNT) / 2)
arrow = pygame.image.load(os.path.join("images", "arrow.png")).convert()
arrow = pygame.transform.scale(arrow, (cycleRadius * 2, cycleRadius * 2))
arrowRed = pygame.image.load(os.path.join("images", "arrow-red.png")).convert()
arrowRed = pygame.transform.scale(arrowRed, (cycleRadius * 2, cycleRadius * 2))
arrowBlue = pygame.image.load(os.path.join("images", "arrow-blue.png")).convert()
arrowBlue = pygame.transform.scale(arrowBlue, (cycleRadius * 2, cycleRadius * 2))

finalFont = pygame.font.SysFont("monospace", 75)
labelsFont = pygame.font.SysFont("monospace", 16)

PLAYER_BUTTON_SIZE = (200, 30)
PLAYER1_BUTTON_POS = ((COLUMN_COUNT * cycleRadius * 2) + 20, 50)
PLAYER2_BUTTON_POS = ((COLUMN_COUNT * cycleRadius * 2) + 20, 100)
START_BUTTON_SIZE = (100, 30)
START_BUTTON_POS = (PLAYER1_BUTTON_POS[0] + 50, 250)

game_running = False
AI_FAKE_TIME = 5


def draw_button(position, size, text, bright_color, color):
    mouse_pos = pygame.mouse.get_pos()
    x = position[0]
    y = position[1]
    width = size[0]
    height = size[1]
    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height and not game_running:
        pygame.draw.rect(screen, bright_color, (x, y, width, height))
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    button_label = labelsFont.render(text, True, BLACK)
    screen.blit(button_label, (x + 5, y + 5))


def refresh_screen():
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(GRAY_FILL)

    mouse_column = int(mouse_pos[0] / (cycleRadius * 2))

    #  draw Arrows
    for column in range(COLUMN_COUNT):
        if column == mouse_column and type(currentPlayer) == Person \
                and game_running and not gameBoard.game_map[0][column]:
            if currentPlayer == player1:
                screen.blit(arrowBlue, (cycleRadius * column * 2, 10))
            else:
                screen.blit(arrowRed, (cycleRadius * column * 2, 10))
        else:
            screen.blit(arrow, (cycleRadius * column * 2, 10))

    #  draw Cycles
    y = int(cycleRadius + SCREEN_HEIGHT / 6)
    for row in gameBoard.game_map:
        x = int(cycleRadius)
        for a in row:
            if a == 0:
                pygame.draw.circle(screen, GRAY, (x, y), cycleRadius - 10)
            elif a == 1:
                pygame.draw.circle(screen, BLUE, (x, y), cycleRadius - 10)
            else:
                pygame.draw.circle(screen, RED, (x, y), cycleRadius - 10)

            x += 2 * cycleRadius
        y += 2 * cycleRadius

    #  draw Buttons

    if type(player1) == Person:
        draw_button(PLAYER1_BUTTON_POS, PLAYER_BUTTON_SIZE, "Player 1: Person", LIGHT_BLUE, BLUE)
    else:  # type(player1) == AI
        draw_button(PLAYER1_BUTTON_POS, PLAYER_BUTTON_SIZE, "Player 1: AI Player", LIGHT_BLUE, BLUE)
    if type(player2) == Person:
        draw_button(PLAYER2_BUTTON_POS, PLAYER_BUTTON_SIZE, "Player 2: Person", LIGHT_RED, RED)
    else:  # type(player2) == AI
        draw_button(PLAYER2_BUTTON_POS, PLAYER_BUTTON_SIZE, "Player 2: AI Player", LIGHT_RED, RED)

    if not game_running:
        draw_button(START_BUTTON_POS, START_BUTTON_SIZE, "Start", LIGHT_GREEN, GREEN)

    pygame.display.flip()


def my_func(position, size, mouse_pos):
    if position[0] < mouse_pos[0] < position[0] + size[0] and position[1] < mouse_pos[1] < position[1] + size[1]:
        return True
    return False


player1 = Person(1)
player2 = Person(2)

currentPlayer = player1

allSlots = COLUMN_COUNT * ROW_COUNT


def run_game():
    global currentPlayer
    global gameBoard
    global game_running
    game_running = True
    currentPlayer = player1
    fake_wait = 0
    dropped_count = 0
    gameBoard = GameBoard()
    while dropped_count != allSlots:
        dropped = False
        if type(currentPlayer) == Person:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.pos[0] < COLUMN_COUNT * cycleRadius * 2:
                        try:
                            input_column = int(ev.pos[0] / (cycleRadius * 2))
                            gameBoard.drop_piece(currentPlayer.number, input_column)
                            dropped = True
                        except Exception as exception:
                            print(exception)

        else:  # currentPlayer == AIPlayer
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()
            fake_wait += 1
            if fake_wait == AI_FAKE_TIME:
                input_column = currentPlayer.get_drop_input(gameBoard.game_map)
                gameBoard.drop_piece(currentPlayer.number, input_column)
                dropped = True

        refresh_screen()

        if dropped:
            fake_wait = 0
            if gameBoard.check_win(currentPlayer.number):
                break
            if currentPlayer == player1:
                currentPlayer = player2
            else:
                currentPlayer = player1
            dropped_count += 1

        clock.tick(30)

    if dropped_count == allSlots:
        label = finalFont.render("Game draw", True, WHITE)
    elif currentPlayer == player1:
        label = finalFont.render("Player 1 won !!", True, LIGHT_BLUE)
    else:
        label = finalFont.render("Player 2 won !!", True, LIGHT_RED)

    screen.blit(label, (40, ROW_COUNT * cycleRadius))
    pygame.display.update()
    pygame.time.wait(1000)
    game_running = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if my_func(PLAYER1_BUTTON_POS, PLAYER_BUTTON_SIZE, event.pos):
                #  player 1 button pressed
                if type(player1) == Person:
                    player1 = AIPlayer(1)
                else:
                    player1 = Person(1)
            elif my_func(PLAYER2_BUTTON_POS, PLAYER_BUTTON_SIZE, event.pos):
                #  player 2 button pressed
                if type(player2) == Person:
                    player2 = AIPlayer(2)
                else:
                    player2 = Person(2)
            elif my_func(START_BUTTON_POS, START_BUTTON_SIZE, event.pos):
                #  start button pressed
                run_game()

    refresh_screen()
    clock.tick(30)

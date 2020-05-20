import os
from game import GameBoard
from player import AIPlayer
from player import Person
import sys
import pygame

gameBoard = GameBoard()

# ----------- py game
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
cycleRadius = int(((SCREEN_HEIGHT - SCREEN_HEIGHT / 6) / len(gameBoard.game_map)) / 2)
arrow = pygame.image.load(os.path.join("images", "arrow.png")).convert()
arrow = pygame.transform.scale(arrow, (cycleRadius * 2, cycleRadius * 2))
arrowRed = pygame.image.load(os.path.join("images", "arrow-red.png")).convert()
arrowRed = pygame.transform.scale(arrowRed, (cycleRadius * 2, cycleRadius * 2))
arrowBlue = pygame.image.load(os.path.join("images", "arrow-blue.png")).convert()
arrowBlue = pygame.transform.scale(arrowBlue, (cycleRadius * 2, cycleRadius * 2))

arrowsColor = [0] * len(gameBoard.game_map[0])

myFont = pygame.font.SysFont("monospace", 75)


def refresh_screen():
    screen.fill((80, 80, 80))
    for column in range(len(gameBoard.game_map[0])):
        if arrowsColor[column] == 0:
            screen.blit(arrow, (cycleRadius * column * 2, 10))
        elif arrowsColor[column] == 1:
            screen.blit(arrowBlue, (cycleRadius * column * 2, 10))
        else:
            screen.blit(arrowRed, (cycleRadius * column * 2, 10))
    y = int(cycleRadius + SCREEN_HEIGHT / 6)
    for row in gameBoard.game_map:
        x = int(cycleRadius)
        for a in row:
            if a == 0:
                pygame.draw.circle(screen, (100, 100, 100), (x, y), cycleRadius - 10)
            elif a == 1:
                pygame.draw.circle(screen, (100, 100, 255), (x, y), cycleRadius - 10)
            else:
                pygame.draw.circle(screen, (255, 100, 100), (x, y), cycleRadius - 10)

            x += 2 * cycleRadius
        y += 2 * cycleRadius

    pygame.display.flip()


# -----------
player1 = Person("player 1", 1)
player2 = AIPlayer("AI player", 2)

currentPlayer = player2

refresh_screen()
droppedCount = 0
allSlots = len(gameBoard.game_map) * len(gameBoard.game_map[0])
while droppedCount != allSlots:
    dropped = False
    if type(currentPlayer) == Person:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                posX = event.pos[0]
                if posX < len(gameBoard.game_map[0]) * cycleRadius * 2:
                    arrowNum = int(posX / (cycleRadius * 2))
                    for i in range(len(arrowsColor)):
                        if arrowNum != i:
                            arrowsColor[i] = 0
                        else:
                            arrowsColor[i] = currentPlayer.number
                else:
                    arrowsColor = [0] * len(gameBoard.game_map[0])

            if event.type == pygame.MOUSEBUTTONDOWN:
                clickX = event.pos[0]
                if clickX < len(gameBoard.game_map[0]) * cycleRadius * 2:
                    try:
                        colInput = int(clickX / (cycleRadius * 2))
                        gameBoard.drop_piece(currentPlayer.number, colInput)
                        arrowsColor = [0] * len(gameBoard.game_map[0])
                        dropped = True
                    except Exception as exception:
                        print(exception)

    else:  # currentPlayer == AIPlayer
        col = currentPlayer.get_drop_input(gameBoard.game_map)
        gameBoard.drop_piece(currentPlayer.number, col)
        dropped = True

    refresh_screen()

    if dropped:
        if gameBoard.check_win(currentPlayer.number):
            break
        if currentPlayer == player1:
            currentPlayer = player2
        else:
            currentPlayer = player1
        droppedCount += 1

if droppedCount == allSlots:
    label = myFont.render("Game draw", 1, (255, 255, 255))
elif currentPlayer == player1:
    label = myFont.render("Player 1 won !!", 1, (100, 100, 255))
else:
    label = myFont.render("Player 2 won !!", 1, (255, 100, 100))

screen.blit(label, (40, 10))
pygame.display.update()
pygame.time.wait(2000)
gameBoard.print_map()
print("GG WP winner : {}".format(currentPlayer.name))

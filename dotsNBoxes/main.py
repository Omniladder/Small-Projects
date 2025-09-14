from gameState import GameState

'''
game = GameState(3,4)

while not game.isGameOver():
    game.printBoard()
    print(game.getMoves())
    initialDot = input("Insert Initial Dot Index ")
    secondDot = input("Insert Second Dot Index ")
    game.playMove(int(initialDot), int(secondDot))

game.printBoard()
print("::GAME OVER::\n\n")
'''
from ai import DotsAI

ai = DotsAI()
ai.solve(4, 4)



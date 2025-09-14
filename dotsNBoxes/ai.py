from gameState import GameState

class DotsAI():
    def __init__(self):
        self.stateStack = []
        self.memoState = {}

    def solve(self, boardWidth, boardHeight):
        initalState = GameState(boardWidth, boardHeight) 
        score = self.explore(initalState, float("-inf"), float("inf"))
        print("Optimal Score " + str(score))

    def explore(self, currentState, alpha, beta):
        hash = currentState.hash()
        if hash in self.memoState:
            return self.memoState[hash]
        if currentState.isGameOver():
            return currentState.score
        value = 0 
        if currentState.playerTurn == 0: # MAX
            value = float("-inf")
            for move in currentState.moveSet: 
                newBoard = currentState.copy()
                newBoard.playMove(move[0], move[1])
                newValue = self.explore(newBoard, alpha, beta)
                alpha = max(alpha, value)
                value = max(newValue, value)
                if beta <= alpha:
                    break
        else: #Min
            value = float("inf")
            for move in currentState.moveSet: 
                newBoard = currentState.copy()
                newBoard.playMove(move[0], move[1])
                newValue = self.explore(newBoard, alpha, beta)
                value = min(newValue, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break

        self.memoState[hash] = value
        return value



class GameState:
    def __init__(self, boardWidth, boardHeight, isCopy = False):
        self.score = 0
        self.playerTurn = 0
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.edges = set()
        self.moveSet = []
        if not isCopy:
            self.generateMoves()

    def generateMoves(self):
        for rowNum in range(self.boardWidth):
            for colNum in range(self.boardHeight):
                dotIndex = rowNum + colNum * self.boardWidth
                rightDot = dotIndex + 1
                lowerDot = dotIndex + self.boardWidth
                if (dotIndex, rightDot) not in self.edges and rowNum < self.boardWidth - 1:
                    self.moveSet.append((dotIndex, rightDot))
                if (dotIndex, lowerDot) not in self.edges and colNum < self.boardHeight - 1:
                    self.moveSet.append((dotIndex, lowerDot))
        
    def getMoves(self):
        return self.moveSet

    def __checkSquare__(self, squareNum):
        leftEdge = (squareNum, squareNum + self.boardWidth) 
        rightEdge = (squareNum + 1, squareNum + self.boardWidth + 1) 
        topEdge = (squareNum, squareNum + 1) 
        bottomEdge = (squareNum + self.boardWidth, squareNum + self.boardWidth + 1) 

        if leftEdge in self.edges and rightEdge in self.edges and topEdge in self.edges and bottomEdge in self.edges:
            if self.playerTurn == 0:
                self.score += 1
            else:
                self.score -= 1

            return True
        return False

    def playMove(self, initialDot, secondDot):


        #Swaps them to be greater dot first for consistency
        if (initialDot > secondDot):
            initialDot, secondDot = secondDot, initialDot


        if ((initialDot, secondDot) not in self.moveSet):
            print("Illegal Move")
            return
        
        self.edges.add((initialDot, secondDot))
        self.moveSet.remove((initialDot, secondDot))
        
        goAgain = False
        # Horizontal Edge
        if secondDot - 1 == initialDot:
            if self.__checkSquare__(initialDot):
                goAgain = True
            if self.__checkSquare__(initialDot - self.boardWidth):
                goAgain = True
        #Vertical Edge
        else:
            if self.__checkSquare__(initialDot):
                goAgain = True
            if self.__checkSquare__(initialDot - 1):
                goAgain = True
        
        if not goAgain:
            self.playerTurn = (self.playerTurn + 1) % 2


    def printBoard(self):
        
        print(f"Player {self.playerTurn + 1} Turn:")
        for y_index in range(self.boardHeight):
            for i in range(2):
                # i = 0 means Horizontal i = 1 means vertical
                for x_index in range(self.boardWidth):
                    dotIndex = x_index + y_index * self.boardWidth
                    rightIndex = dotIndex + 1
                    lowerIndex = dotIndex + self.boardWidth
                    
                    if (dotIndex, rightIndex) not in self.edges and i == 0:
                        print("+ ", end="")
                    elif i == 0:
                        print("+-", end="")
                    elif (dotIndex, lowerIndex) in self.edges:
                        print("| ", end="")
                    else:
                        print("  ", end="")
                print("")
        print(f"\nCurrent Score: {self.score}")
                
    def isGameOver(self):
        if self.getMoves() == []:
            return True
        else:
            return False

    def getTurn(self):
        return self.playerTurn

    def copy(self):
        newCopy = GameState(self.boardWidth, self.boardHeight, True)
        newCopy.score = self.score
        newCopy.edges = self.edges.copy()
        newCopy.moveSet = self.moveSet.copy()
        newCopy.playerTurn = self.playerTurn
        return newCopy

    def hash(self):
        hash = str(self.playerTurn) + " "
        for move in self.moveSet:
            moveHash = str(move[0]) + " , " + str(move[1])
            hash = hash + moveHash + " "
        return hash

    def __str__(self):
        return self.hash()






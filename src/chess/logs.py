import os
from src.chess import chess

class GameLog:
    def __init__(self, filename="stdout"):
        if filename != "stdout":
            filename = os.path.join(os.getcwd(), "logs", filename)
        self.filename = filename

    # print metadata
    def LogMetadata(self, metadata):
        if self.filename == "stdout":
            print(metadata)
        else:
            with open(self.filename, "w") as file:
                file.write(str(metadata)+"\n")

    # print move
    def LogMove(self, src, dest, colour):
        logstr = str(src[0])+","+str(src[1])+"-"+str(dest[0])+","+str(dest[1])
        if colour == chess.WHITE:
            logstr += " "
        else:
            logstr += "\n"
        
        if self.filename == "stdout":
            print(logstr, end="")
        else:
            with open(self.filename, "a") as file:
                file.write(logstr)

    # end game
    def LogGameEnd(self, winner):
        logstr = "Winner: " + str(winner)
        if self.filename == "stdout":
            print(logstr)
        else:
            with open(self.filename, "a") as file:
                file.write(logstr)

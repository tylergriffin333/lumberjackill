from tileStone import TileStone
from jack import Jack
from evilTree import EvilTree

def genEntFromChar(char, x, y, game):
    if char==" ":
        game.addTile(None, x, y)
    elif char=="J":
        game.addEntity(Jack(game, x, y))#maybe entities should know how to add themselves to the game, so I don't have to know if they're a tile or a dynamic entity here.
    elif char=="T":
        game.addEntity(EvilTree(game, x, y))#maybe entities should know how to add themselves to the game, so I don't have to know if they're a tile or a dynamic entity here.
    else:
        game.addTile(TileStone(game, x, y), x, y)

def getMapDimensionsFromMapFile(filename):
    file = open(filename, "r")
    
    height=0
    width=0
    
    for line in file:
        height+=1
        width=len(line)+2
        
    return [width, height]

def loadMap(filename, game):
    file = open(filename, "r")

    x=0
    y=0

    for line in file:
        x=0
        for char in line:
            genEntFromChar(char, x, y, game)
            x+=1
        y+=1
        
    file.close()
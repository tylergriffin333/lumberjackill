#the screen class should be used to:
    #keep track of the current screen position relative to the game world,
    #keep track of items in the world that are currently "on screen" so that we only render graphics and audio for the items we can see,
    #render the HUD and pause menu. 

from posDimEntity import PosDimEntity

class Screen(PosDimEntity):
    def __init__(self, x, y, width, height):
        PosDimEntity(self, x, y, width, height)
from posDimEntity import PosDimEntity
from rectColliderDynamic import RectColliderDynamic
from imageRenderer import ImageRenderer

class Jack(PosDimEntity, ImageRenderer, RectColliderDynamic):
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, .48, .75)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        ImageRenderer.__init__(self, game.graphicsRenderer, "jack.png")
        
        self.speed=.005
        #self.image1=self.image
        #self.image2=self.graphicsRenderer.loadImage("jack2.png")
        
#     def isCollidingWithRect(self, otherRect):
#         isColliding=RectColliderDynamic.isCollidingWithRect(self, otherRect)
#           
#         if isColliding:
#             self.image=self.image1
#             print(str(self.game.delta))
#         else:
#             self.image=self.image2
#           
#         return isColliding
        
    def run(self):
        if self.game.input.left: self.x-=self.speed*self.game.delta
        if self.game.input.right: self.x+=self.speed*self.game.delta
        if self.game.input.up: self.y-=self.speed*self.game.delta
        if self.game.input.down: self.y+=self.speed*self.game.delta
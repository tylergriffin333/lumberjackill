from entity import Entity

class Baddie(Entity):
    def __init__(self, game):
        Entity.__init__(self, game, "baddie")
        
    def hitTop(self, otherCollider):
        if otherCollider.team=="jack":
            self.game.removeEntity(self)
            
    def hitBot(self, otherCollider):
        if otherCollider.team=="jack":
            if otherCollider.isChopping():
                self.game.removeEntity(self)
                
    def hitRight(self, otherCollider):
        if otherCollider.team=="jack":
            if otherCollider.isChopping() and otherCollider.facingRight==False:
                self.game.removeEntity(self)
            else:
                pass#TODO: hurt jack here
            
    def hitLeft(self, otherCollider):
        if otherCollider.team=="jack":
            if otherCollider.isChopping() and otherCollider.facingRight:
                self.game.removeEntity(self)
            else:
                pass#TODO: hurt jack here
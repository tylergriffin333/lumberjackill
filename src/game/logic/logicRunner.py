from gameModule import GameModule

class LogicRunner(GameModule):
    def __init__(self, game):
        GameModule.__init__(self, game)
        self.reqAttr="run"#required attribute for entities to have to be added to entities or tiles lists
        
    def run(self):
        for entity in self.entities:
            entity.run()
            
        for column in self.tiles:
            for tile in column:
                if tile != None:
                    tile.run()
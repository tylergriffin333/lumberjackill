class CollisionSystem():
    def __init__(self, game):
        self.game=game
        self.entities=[]#renderers
        self.tiles=[]
    
    def instantiateTilesArray(self, width, height):#TODO: this is replicated between gameMain, collisionSystem, and graphicsRenderer
        self.tiles=[]

        for x in range(width):
            column=[]
            for y in range(height):
                column.append(None)
            self.tiles.append(column)
            
    def addTile(self, tile, x, y):#TODO: this is replicated between gameMain, collisionSystem, and graphicsRenderer
        if hasattr(tile, "isCollidingWith"):
            self.tiles[x][y]=tile
        
    def addEntity(self, entity):#TODO: this is replicated between gameMain, collisionSystem, and graphicsRenderer
        if hasattr(entity, "isCollidingWith"):
            self.entities.append(entity)
    
    ###############################################################################################################################################
    #####collision detection#######################################################################################################################
    
    def isRectCollidingWithRect(self, rect1, rect2):
        return rect1.left<rect2.right and rect1.right>rect2.left and rect1.top<rect2.bottom and rect1.bottom>rect2.top
    
    ###############################################################################################################################################
    #####collision handling########################################################################################################################
    
    def handleRectVsRectCollision(self, rect1, rect2, rect1MoveRatio):#rect1MoveRatio must be 0<=rect1MoveRatio<=1
        #pass
        rect2MoveRatio=1-rect1MoveRatio#these ratios will always add up to 1.  each denotes how much of the required "scootching" each rectangle will do so they're no longer overlapping.
     
        rightOverlap=rect1.right-rect2.left
        leftOverlap=rect2.right-rect1.left
        topOverlap=rect2.bottom-rect1.top
        bottomOverlap=rect1.bottom-rect2.top
         
        if rightOverlap<leftOverlap and rightOverlap<topOverlap and rightOverlap<bottomOverlap:#is rightOverlap the smallest?
            rect1.x-=rightOverlap*rect1MoveRatio
            rect2.x+=rightOverlap*rect2MoveRatio
            rect1.hitRight(rect2)
            rect2.hitLeft(rect1)
        elif leftOverlap<topOverlap and leftOverlap<bottomOverlap:#is leftOverlap the smallest?
            rect1.x+=leftOverlap*rect1MoveRatio
            rect2.x-=leftOverlap*rect2MoveRatio
            rect1.hitLeft(rect2)
            rect2.hitRight(rect1)
        elif topOverlap<bottomOverlap:#is topOverlap the smallest?
            rect1.y+=topOverlap*rect1MoveRatio
            rect2.y-=topOverlap*rect2MoveRatio
            rect1.hitTop(rect2)
            rect2.hitBottom(rect1)
        else:#bottomOverlap is the smallest
            rect1.y-=bottomOverlap*rect1MoveRatio
            rect2.y+=bottomOverlap*rect2MoveRatio
            rect1.hitBottom(rect2)
            rect2.hitTop(rect1)
    
    def handleDynamicRectVsDynamicRectCollision(self, dynamicRect1, dynamicRect2):
        self.handleRectVsRectCollision(dynamicRect1, dynamicRect2, .5)
    
    def handleDynamicRectVsStaticRectCollision(self, dynamicRect, staticRect):
        self.handleRectVsRectCollision(dynamicRect, staticRect, 1)
        
    ###############################################################################################################################################
    #####run#######################################################################################################################################
    
    def run(self):
        self.runCollision()
    
    def runCollision(self):
        for entity1 in self.entities:
            for entity2 in self.entities:
                if entity1 != entity2:
                    if entity1.isCollidingWith(entity2):
                        entity1.handleCollision(entity2)
        
        for column in self.tiles:
            for tile in column:
                if tile != None:
                    for entity in self.entities:
                        if tile.isCollidingWith(entity):
                            tile.handleCollision(entity)
                            #entity.handleCollision(tile)
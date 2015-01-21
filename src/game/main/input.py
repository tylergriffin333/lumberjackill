import pygame
import utils

#TODO: there should be a proxy between this class and the platform-specific code (pygame right now)

class Input():#TODO: should this inherit from gameModule?
    def __init__(self, game):
        pygame.init()#TODO: find a way to check to see if this has already been done
        self.game=game
        self.left=False
        self.right=False
        self.down=False
        self.up=False
        #self.leftMouse=False
        #self.curMouseScreenPos=[0, 0]
        
    @property
    def curMouseScreenX(self):
        return self.curMouseScreenPos[0]
    
    @property
    def curMouseScreenY(self):
        return self.curMouseScreenPos[1]
        
    def run(self):
        self.handleEvents()
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                utils.exit()
            elif event.type==pygame.KEYDOWN:
                self.keyPressed(event)
            elif event.type==pygame.KEYUP:
                self.keyReleased(event)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                self.mousePressed(event)
            elif event.type==pygame.MOUSEBUTTONUP:
                self.mouseReleased(event)
            elif event.type==pygame.MOUSEMOTION:
                self.mouseMoved(event)
    
    def keyPressed(self, e):
        code=e.key
        
        if code==pygame.K_ESCAPE: utils.exit()
        elif code==pygame.K_a or code==pygame.K_LEFT: self.left=True
        elif code==pygame.K_s or code==pygame.K_DOWN: self.down=True
        elif code==pygame.K_d or code==pygame.K_RIGHT: self.right=True
        elif code==pygame.K_w or code==pygame.K_UP: self.up=True
            
    def keyReleased(self, e):
        code=e.key
        
        if code==pygame.K_ESCAPE: utils.exit()
        elif code==pygame.K_a or code==pygame.K_LEFT: self.left=False
        elif code==pygame.K_s or code==pygame.K_DOWN: self.down=False
        elif code==pygame.K_d or code==pygame.K_RIGHT: self.right=False
        elif code==pygame.K_w or code==pygame.K_UP: self.up=False
        
    def mouseMoved(self, e):
        #self.curMouseScreenPos=e.pos
        #self.game.uiLogic.mouseMoved(e.pos)
        pass
    
    def mousePressed(self, e):
        #self.curMouseScreenPos=e.pos
        #button=e.button
        
        #if button==1:
        #    self.leftMouse=True
        #    self.game.uiLogic.leftMouseDown(e.pos)
        #elif button==3:
        #    self.game.uiLogic.rightMouseDown(e.pos)
        pass
        
    def mouseReleased(self, e):
        #self.curMouseScreenPos=e.pos
        #button=e.button
        
        #if button==1:
        #    self.leftMouse=False
        #    self.game.uiLogic.leftMouseUp(e.pos)
        pass
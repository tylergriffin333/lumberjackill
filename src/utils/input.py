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
        self.jump=False
        self.joyAxisX=0.0
        self.joyAxisY=0.0
        self.running=False
        self.attack=False
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
                joystick.init()
        #self.leftMouse=False
        #self.curMouseScreenPos=[0, 0]
        
    @property
    def curMouseScreenX(self):
        return self.curMouseScreenPos[0]
    
    @property
    def curMouseScreenY(self):
        return self.curMouseScreenPos[1]
        
    def run(self):
        self.handleInputEvents()
        
    def handleInputEvents(self):
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
            elif event.type==pygame.JOYAXISMOTION:
                self.joystickMoved(event)
            elif event.type==pygame.JOYBUTTONDOWN:
                self.joystickButtonPressed(event)
            elif event.type==pygame.JOYBUTTONUP:
                self.joystickButtonReleased(event)
    
    def joystickButtonReleased(self, event):
        if event.button==13: self.left=False
        elif event.button==14: self.right=False
        elif event.button==0: self.jump=False
        elif event.button==2: self.running=False
    
    def joystickButtonPressed(self, event):
        if event.button==13: self.left=True
        elif event.button==14: self.right=True
        elif event.button==0: self.jump=True
        elif event.button==2: self.running=True
    
    def joystickMoved(self, event):
        if event.axis==0: self.joyAxisX=event.value
        if event.axis==1: self.joyAxisY=event.value
        #print(str(self.joyAxisX)+", "+str(self.joyAxisY))
    
    def keyPressed(self, e):
        code=e.key
        
        if code==pygame.K_ESCAPE: utils.exit()
        elif code==pygame.K_a or code==pygame.K_LEFT: self.left=True
        elif code==pygame.K_s or code==pygame.K_DOWN: self.down=True
        elif code==pygame.K_d or code==pygame.K_RIGHT: self.right=True
        elif code==pygame.K_w or code==pygame.K_UP: self.jump=True
        elif code==pygame.K_LSHIFT or code==pygame.K_RSHIFT: self.running=True
        elif code==pygame.K_SPACE or code==pygame.K_f: self.attack=True
            
    def keyReleased(self, e):
        code=e.key
        
        if code==pygame.K_ESCAPE: utils.exit()
        elif code==pygame.K_a or code==pygame.K_LEFT: self.left=False
        elif code==pygame.K_s or code==pygame.K_DOWN: self.down=False
        elif code==pygame.K_d or code==pygame.K_RIGHT: self.right=False
        elif code==pygame.K_w or code==pygame.K_UP: self.jump=False
        elif code==pygame.K_LSHIFT or code==pygame.K_RSHIFT: self.running=False
        elif code==pygame.K_SPACE or code==pygame.K_f: self.attack=False
        
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
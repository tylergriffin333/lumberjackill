from renderer import Renderer

class ImageRenderer(Renderer):
    def __init__(self, graphicsRenderer, imageFilename, xOffset=0, yOffset=0):
        Renderer.__init__(self, graphicsRenderer)
        self.image=self.graphicsRenderer.loadImage(imageFilename, 1)
        self.xOffset=xOffset
        self.yOffset=yOffset
        
    def render(self):
        #self.graphicsRenderer.drawImage(self.image, self.x, self.y)
        self.graphicsRenderer.drawImage(self.image, self.left, self.top+self.yOffset, self.width+self.xOffset, self.height)
        #self.graphicsRenderer.drawRect(self)
        
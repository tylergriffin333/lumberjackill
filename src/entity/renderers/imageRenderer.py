from renderer import Renderer

class ImageRenderer(Renderer):
    def __init__(self, graphicsRenderer, imageFilename):
        Renderer.__init__(self, graphicsRenderer)
        self.image=self.graphicsRenderer.loadImage(imageFilename)
        
    def render(self):
        self.graphicsRenderer.drawImage(self.image, self.left, self.top)
        #self.graphicsRenderer.drawRect(self)
        
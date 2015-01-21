from renderer import Renderer
import assetLoader
import utils

class ImageAnimationRenderer(Renderer):
    def __init__(self, graphicsRenderer, animationFilename):
        Renderer.__init__(self, graphicsRenderer)
        imageNames=assetLoader.loadAnimation(animationFilename, self)
        self.totalAnimationLength=self.uniformFrameLength*len(imageNames)
        self.timeOffset=utils.getRandom()*self.totalAnimationLength
        self.rightImages=graphicsRenderer.loadImages(imageNames)
        self.leftImages=graphicsRenderer.loadImagesFlippedHorizontally(imageNames)
        
    def getCurImage(self):
        curFrame=(utils.getCurMilliseconds()%self.totalAnimationLength)/len(self.rightImages)
        
        if self.xVel>0:
            return self.rightImages[curFrame]
        else:
            return self.leftImages[curFrame]
        
    def render(self):
        self.graphicsRenderer.drawImage(self.getCurImage(), self.left, self.top+self.yOffset, self.width+self.xOffset, self.height)
        #self.graphicsRenderer.drawImage(self.getCurImage(), self.left, self.top, self.width, self.height)
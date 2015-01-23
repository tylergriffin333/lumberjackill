#TODO: create an "Animation" class.  there should be one animation class for every animation file loaded.
    #each imageAnimationRenderer should have one to many animation class instances (animations)
    #the animationLoader.loadAnimation() function should accept only an animation file name, and return only an animation instance
    #the animationLoader should be able to handle fixed-frame-length animations, or animations with different lengths to display different frames.
    #imageAnimationRenderer should be able to use different x and y offsets for different animations.
    #each type of animated entity should have it's own extension of imageAnimationRenderer, rather than extending imageAnimationRenderer directly.
        #for example, the tree class should not pass animation file paths to imageAnimationRenderer.  that information should be stored in treeAnimationRenderer, which should extend imageAnimationRenderer.
    #each .animation file (and associated animation class instance) should have a name to make the animation-switching code more readable.
        #ImageAnimationRenderer can create a map to associate the name to the index in it's "animations" array.

#TODO: need to make shared resources between animation and imageRenderer instances static.  right now I'm loading the same images multiple times. 

from renderer import Renderer
import assetLoader
import utils

class ImageAnimationRenderer(Renderer):
    def __init__(self, graphicsRenderer, animationFilename):
        Renderer.__init__(self, graphicsRenderer)
        imageNames=assetLoader.loadAnimation(animationFilename, self)
        self.totalAnimationLength=self.uniformFrameLength*len(imageNames)
        self.timeOffset=int(utils.getRandom()*self.totalAnimationLength)
        self.rightImages=graphicsRenderer.loadImages(imageNames)
        self.leftImages=graphicsRenderer.loadImagesFlippedHorizontally(imageNames)
        
    def getCurImage(self):
        curFrame=((utils.getCurMilliseconds()+self.timeOffset)%self.totalAnimationLength)/self.uniformFrameLength
        
        if self.xVel>0:
            return self.rightImages[curFrame]
        else:
            return self.leftImages[curFrame]
        
    def render(self):
        self.graphicsRenderer.drawImage(self.getCurImage(), self.left, self.top+self.yOffset, self.width+self.xOffset, self.height)
        #self.graphicsRenderer.drawImage(self.getCurImage(), self.left, self.top, self.width, self.height)
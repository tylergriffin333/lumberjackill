#TODO: create an "Animation" class.  there should be one animation class for every animation file loaded.
    #each imageAnimationRenderer should have one to many animation class instances (animations)
    #the animationLoader.loadAnimation() function should accept only an animation file name, and return only an animation instance
    #the animationLoader should be able to handle fixed-frame-length animations, or animations with different lengths to display different frames.
    #imageAnimationRenderer should be able to use different x and y offsets for different animations.
    #each type of animated entity should have it's own extension of imageAnimationRenderer, rather than using imageAnimationRenderer directly.
        #for example, the tree class should not pass animation file paths to imageAnimationRenderer.  that information should be stored in treeAnimationRenderer, which should extend imageAnimationRenderer.
    #each extension of imageAnimationRenderer should store each animation under it's own variable, with a unique name that identifies that animation.
        #so you would load the "animations/evil_tree/running.animation" file into the: evilTreeImageAnimationRenderer.running variable

#TODO: need to make shared resources between animation instances static.  right now I'm loading the same images multiple times. 

from renderer import Renderer
import assetLoader
import utils

class ImageAnimationRenderer(Renderer):
    def __init__(self, graphicsRenderer, animationFilename):
        Renderer.__init__(self, graphicsRenderer)
        imageNames=assetLoader.loadAnimation(animationFilename, self)
        self.totalAnimationLength=self.uniformFrameLength*len(imageNames)
        self.timeOffset=int(utils.getRandom()*self.totalAnimationLength)
        self.images=self.graphicsRenderer.loadImages(imageNames)
        
    def getCurImage(self):
        curFrame=((utils.getCurMilliseconds()+self.timeOffset)%self.totalAnimationLength)/self.uniformFrameLength
        return self.images[curFrame]
        
    def render(self):
        if self.xVel>0: self.graphicsRenderer.drawImage(self.getCurImage(), self.left, self.top+self.yOffset, self.width+self.xOffset, self.height)
        else: self.graphicsRenderer.drawImageFlippedHorizontally(self.getCurImage(), self.left, self.top+self.yOffset, self.width+self.xOffset, self.height)
        #self.graphicsRenderer.drawImage(self.getCurImage(), self.left, self.top, self.width, self.height)
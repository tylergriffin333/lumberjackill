#this class will represent a single image animation, loaded from a single animation file
    #for example, an instance of this class might represent the evil tree running animation.
    #for animations with only two directions (left and right or up and down), only one set of images should be stored, that can be dynamically flipped for the opposite direction.

import assetLoader
import utils

class ImageAnimation():
    def __init__(self, graphicsRenderer, animationFilename):
        imageNames=assetLoader.loadAnimation(animationFilename, self)
        self.totalAnimationLength=self.uniformFrameLength*len(imageNames)
        self.timeOffset=int(utils.getRandom()*self.totalAnimationLength)
        self.images=graphicsRenderer.loadImages(imageNames)
    
    def getCurImage(self, curMilliseconds):
        curFrame=((curMilliseconds+self.timeOffset)%self.totalAnimationLength)/self.uniformFrameLength
        return self.images[curFrame]
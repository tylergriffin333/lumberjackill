#this class will represent a single image animation, loaded from a single animation file
    #for example, an instance of this class might represent the evil tree running animation.
    #for animations with only two directions (left and right or up and down), only one set of images should be stored, that can be dynamically flipped for the opposite direction.

import assetLoader
import utils

class ImageAnimation():
    def __init__(self, graphicsRenderer, animationFilename, scale):
        imageNames, self.frameLengths=assetLoader.loadAnimationData(animationFilename)#get image names and frame lengths from .animation file
        self.images=graphicsRenderer.loadImages(imageNames, scale)#load images
        self.totalAnimationLength=sum(self.frameLengths)
    
    def getCurImage(self):
        curFrame=0
        totalMilliseconds=0
        
        for frameLength in self.frameLengths:
            totalMilliseconds+=frameLength
            
            if((utils.getCurMilliseconds()-self.startTime)%self.totalAnimationLength<totalMilliseconds):
                return self.images[curFrame]
            
            curFrame+=1
            
        return self.images[-1]#return the last image in the list
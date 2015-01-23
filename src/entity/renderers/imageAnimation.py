#this class will represent a single image animation, loaded from a single animation file
    #for example, an instance of this class might represent the evil tree running animation.
    #for animations with only two directions (left and right or up and down), only one set of images should be stored, that can be dynamically flipped for the opposite direction.

class ImageAnimation():
    def __init__(self, animationFilename):
        #.animation file should be loaded here
        pass
    
    def getCurImage(self, milliseconds):
        #the milliseconds will usually be the global system time in milliseconds plus some offset unique to the calling instance of imageAnimationRenderer.
            #the offset keeps separate instances of same-type entities from having synchronized animations.
        pass
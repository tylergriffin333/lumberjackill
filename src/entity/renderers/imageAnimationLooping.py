from imageAnimation import ImageAnimation
import utils

class ImageAnimationLooping(ImageAnimation):
    def __init__(self, graphicsRenderer, animationFilename, scale):
        ImageAnimation.__init__(self, graphicsRenderer, animationFilename, scale)
        self.startTime=int(utils.getRandom()*self.totalAnimationLength)
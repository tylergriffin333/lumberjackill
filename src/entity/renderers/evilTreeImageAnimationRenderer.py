from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimation import ImageAnimation

class EvilTreeImageAnimationRenderer(ImageAnimationRenderer):
    def __init__(self, graphicsRenderer):
        ImageAnimationRenderer.__init__(self, graphicsRenderer)
        self.runningAnimation=ImageAnimation(graphicsRenderer, "evil_tree/running.animation")
        self.curAnimation=self.runningAnimation
#import rabbyt
#print rabbyt.__file__

from game import Game

Game().run()

# from graphicsProxyRabbyt import GraphicsProxyRabbyt
#  
# graphicsProxy=GraphicsProxyRabbyt()
# jackImage=graphicsProxy.loadImage("jack.png", 1)
#  
# while True:
#     graphicsProxy.fillBackground([1, 1, 1])
#     graphicsProxy.drawImage(jackImage, 0, 0)
#     graphicsProxy.swapBuffer()
import constants

def loadAnimation(filename, imageAnimationRenderer):    
    file = open(filename, "r")

    inImageNames=False
    path=None
    imageNames=[]

    for line in file:
        if not line.startswith("#"):
            if not inImageNames:
                if line.startswith("path="):
                    path=line[5:].rstrip()
                elif line.startswith("recommended_entity_width="):
                    imageAnimationRenderer.width=float(line[25:])/constants.pixelToGameUnitRatio
                elif line.startswith("recommended_entity_height="):
                    imageAnimationRenderer.width=float(line[26:])/constants.pixelToGameUnitRatio
                elif line.startswith("xOffset="):
                    imageAnimationRenderer.xOffset=float(line[8:])/constants.pixelToGameUnitRatio
                elif line.startswith("yOffset="):
                    imageAnimationRenderer.yOffset=float(line[8:])/constants.pixelToGameUnitRatio
                elif line.startswith("uniformFrameLength="):
                    imageAnimationRenderer.uniformFrameLength=int(line[19:])
                elif line.startswith("images="):
                    inImageNames=True
            else:
                imageNames.append(path+line.rstrip())
        
    file.close()
    return imageNames

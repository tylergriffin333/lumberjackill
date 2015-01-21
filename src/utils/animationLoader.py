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
                elif line.startswith("xOffset="):
                    imageAnimationRenderer.xOffset=float(line[8:])
                elif line.startswith("yOffset="):
                    imageAnimationRenderer.yOffset=float(line[8:])
                elif line.startswith("uniformFrameLength="):
                    imageAnimationRenderer.uniformFrameLength=int(line[19:])
                elif line.startswith("images="):
                    inImageNames=True
            else:
                imageNames.append(path+line.rstrip())
        
    file.close()
    return imageNames
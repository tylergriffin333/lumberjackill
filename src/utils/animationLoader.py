def loadAnimationData(filename):    
    file = open(filename, "r")

    imageNames=[]
    frameLengths=[]

    for line in file:
        if not line.startswith("#"):
            data=line.rstrip().split(',')
            imageNames.append(data[0])
            frameLengths.append(int(data[1]))
        
    file.close()
    return imageNames, frameLengths
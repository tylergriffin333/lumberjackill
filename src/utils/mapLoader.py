def loadMap(filename):
    file = open(filename, "r")

    mapArray=[]
     
    firstLine=file.readline()
     
    for char in range(len(firstLine)-1):
        column=[]
        column.append(firstLine[char])
        mapArray.append(column)#create a column for every char we find in the first line
     
    for line in file:
        for column in range(len(mapArray)):
            mapArray[column].append(line[column])
         
    for y in range(len(mapArray[0])):
        stringLineOut=""
        for x in range(len(mapArray)):
            stringLineOut+=mapArray[x][y]
        print(stringLineOut)
        
    file.close()
    
    return mapArray#TODO: make this function return
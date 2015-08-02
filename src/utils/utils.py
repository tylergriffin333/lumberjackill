import math
import random
import sys
import time

Tau=math.pi*2
PI=math.pi
E=math.e

def sqrt(n):
    return math.sqrt(n)

def atan2(y, x):
    return math.atan2(y, x)

def cos(a):
    return math.cos(a)

def sine(a):
    return math.sin(a)

def abs(n):
    return math.fabs(n)

def pow(n, p):
    return math.pow(n, p)

def getRandom():
    return random.random()

def getRandomIntZeroMax(max):
    return getRandomIntInRange(0, max)

def getRandomIntInRange(min, max):
    return random.randint(min, max)
    
def exit():
    sys.exit()
    
def getDifBetweenDirs(dir1, dir2):#returns the minimum angle(could be left or right/pos or neg) that dir1 needs to turn to be facing dir2
    dir1=fixRot(dir1)
    dir2=fixRot(dir2)
    
    if dir2<dir1:
        right=dir1-dir2#add this to dir1 to be facing dir2
        left=Tau-right
    else:
        left=dir2-dir1
        right=Tau-left
        
    if left>right: return -right
    else: return left

def getPoissonRand():
    rand=getRandom()
    return pow(E,-1)/factorial(rand)

def factorial(num):
    result=1
    while num>0:
        result*=num
        num-=1
    return result

def distSqrd(x1, y1, x2, y2):
    return pow(x1-x2, 2)+pow(y1-y2, 2)

def dist(x1, y1, x2, y2):
    return sqrt(distSqrd(x1, y1, x2, y2))

def fixRot(rot):#returns rot so 0<=rot<2PI
    rot=rot%(Tau)
    if rot<=0: rot+=Tau#now 0<=rot<2PI
    return rot

def getDirFromPointToPoint(fromX, fromY, toX, toY):
    return fixRot(atan2(toY-fromY, toX-fromX))

def getVelFromPointToPoint(fromX, fromY, toX, toY):
    distance=dist(fromX, fromY, toX, toY)
    xVel=(toX-fromX)/distance
    yVel=(toY-fromY)/distance
    return [xVel, yVel]

def getCurMilliseconds():
    return int(round(time.time() * 1000))

def transformPoint(x, y, rot, globalScale, localScale, point):
    retPoint=[]
    
    retPoint.append((point[0]*cos(rot)-point[1]*sine(rot))*localScale*globalScale+x*globalScale)
    retPoint.append((point[0]*sine(rot)+point[1]*cos(rot))*localScale*globalScale+y*globalScale)
    
    return retPoint
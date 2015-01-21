#this module will be used to load assets (images, sounds, ect...) from disk into memory
import pygame
#import rabbyt

assetsDir="../../../assets/"

def loadImage(filename):
    return pygame.image.load(assetsDir+"images/"+filename)#rabbyt.Sprite(filename)

def loadSound(filename):
    return pygame.mixer.Sound(assetsDir+"sounds/"+filename)
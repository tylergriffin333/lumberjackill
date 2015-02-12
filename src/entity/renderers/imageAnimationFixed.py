#TODO: the only thing in the .animation files should be a list of the images in sequence, and each of their frame-lengths if it's not uniform frame-lengths
    #this class will be for non-looping animations.
        #reset() function: it need to be able to be reset to the beginning of the animation
        #isOver() function: returns boolean.  you'll need to know when the animation is over.
        #later I may need to add the capability for this class to call back to the parent to tell it that it's time for some action.
            #maybe self.parent.performAction(self)
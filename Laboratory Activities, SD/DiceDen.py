from die import die
class Player(object):
    def __init__(self):
        """Has a pair of dice and an empty roll list."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        
    def __str__(self):
        """returns a string representation of the list of rolls."""
    result = ""
    for (v2,v2) in self.rolls:
        result = result + str((v1,v2)) + ""+\
        str(v1 + v2) + "\n"
    
    def getNumberOfRolls(self):
        """Return the number of the rolls."""
        return len(self.rolls)
        
    def play(self):
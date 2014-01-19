from ai import AI
from abc import *

class Entities(AI):    
    __metaclass__ = ABCMeta 

    def __init__ (self, spawn, health, max_dmg , min_dmg):
        """
            spawn - 2-tuple (x,y)
            dmg - int
            health - int 
            
        """
        self.idling = True
        self.attacking = False
        self.spawn = spawn
        self.health = health
        self.max_dmg = max_dmg
        self.min_dmg = min_dmg
        self.invinc = False
        self.in_action = False 
        self.parrys = False
        self.sight = 80 # pxs away from the center of the entity
        self.attack_friendly = False
        self.can_jump = True
        self.flying = False
        self.escaping = False
        self.escape_threshold = 0
        
    def jump(self):
        pass
        #add code here
     
    @abstractproperty
    def sprite (self):
        """ sprite should be an instance of  pygame.sprite
        """
        pass
      
    @abstractproperty
    def attack_max_frame(self):
        pass
    
    @abstractproperty
    def action_max_frame(self):
        pass
    
    @abstractproperty
    def discover_max_frame(self):
        """ Will be used iftp
        """
        pass
    
def main():
    print "This class shouldn't be ran to start the game, the following is a test."
    a = Entities(1,2,0)
    print a.invinc
    
main()
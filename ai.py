from abc import *

class AI:
    """ The base AI class. Entity classes inherit from this.
        Instantiated from it to make specific AIs
        Each subclass must have the following, or they can't be instan:
        react_attack()
        idle()
        attack()
        action()
        escape()
        on_discover()
        on_death()
    """
    __metaclass__ = ABCMeta 
    
    def __init__(self,direction,jump_interval):
        self.direction = 0 # 0 is left 1 is right
        self.jump_interval = 0 # interval at which the entity jumps
        
    @abstractmethod
    def react_attack(self):
        """ called after attacked
        """
        pass
    
    @abstractmethod
    def idle(self):
        """ used when main char is not in sight
        """
        pass
    
    @abstractmethod
    def attack(self):
        """normal attacks 
        """
        pass
    
    @abstractmethod
    def action(self):
        """special action
        """
        pass

    def escape(self):
        """move away from player
        a move method in the main class. jump in front of obstacles etc.
        when health fall through escape_threshold
        """
        self.escaping = True
    
    @abstractmethod
    def on_discover(self):
        """called when entity enters the screen
        """
        pass
    
    @abstractmethod
    def on_death(self):
        """called right after entity after killed
        """
        pass
        
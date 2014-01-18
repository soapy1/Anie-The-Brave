import pygame 
import logging
    
class LevelManager:
    """ handle level files.
    """
    land = 'A'
    mage_spawn = 'M'
    player_spawn = 'S'
    warrior_spawn = 'W'
    paladin_spawn = 'P'
    
    def __init__(self):
        self.levels = {}
        
    def load_level(self,file_name):
        """filename - the name of level to load.
        """
        level_file = open(file_name,'r')
        as_list = []
        for line in level_file:
            as_list.append([x for x in line.strip()])
        self.levels[file_name] = as_list
    
    def get_level(self,level_name):
        try:
            return self.levels[level_name]
        except KeyError: 
            return None
        
    def interpret(self,name):
        """interpret a loaded level
           return a list of pygame.rect object, representing the landscape 
           of the level
        """
        rect_list = []
        level = self.levels[name]
        for line in range(len(level)):
            for char in range(len(level[line])):
                if level[line][char] == self.land:
                    width = 1
                    height = 1 
                    tmp_char = char
                    temp_line = line
                    while True:
                        try:
                            if level[line][tmp_char] == self.land:
                                width += 1
                                level[line][tmp_char] = None
                            else: 
                                break
                            tmp_char += 1
                        except IndexError:
                            break
                    while True:
                        try:
                            if level[temp_line][char] == self.land:
                                height += 1
                                level[temp_line][char] = None
                            else: 
                                break
                            temp_line+=1
                        except IndexError:
                            break
                    rect_list.append(pygame.rect.Rect(line*20,char*20,width*20,height*20))
        return rect_list
    
    def info(self):
        print "%d levels loaded" % len(self.levels)
        logging.info("%d levels loaded" % len(self.levels))
        
def main():
    a = LevelManager()
    a.load_level("meow")
    #print a.get_level("meow")
    print a.interpret("meow")
main()
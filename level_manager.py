"""
Originally Written in Great Canadian Appathon 2014.
"""
import pygame.rect as rect


class LevelManager:
    """ handle level files.
    """
    land = 'A'
    mage_spawn = 'M'
    player_spawn = 'S'
    warrior_spawn = 'W'
    paladin_spawn = 'P'
    
    def __init__(self):
        """ initialize the level manager.
            screen_res - The resolution of the game (width, height)
        """
        self.levels = {}
        self.current_level = -1
        
    def load_level(self,file_name):
        """filename - the name of level to load.
        """
        level_file = open(file_name,'r')
        as_list = []
        for line in level_file:
            as_list.append([x for x in line.strip()])
        self.levels[file_name] = as_list
            
    def next_level(self):
        if len(self.levels) >= self.current_level+1:
            self.current_level += 1
            return self.levels[self.levels.keys()[self.current_level]] #list indices start at 0, so current level is -1
            
        return None
    
    def get_current_dimensions(self):
        return len(self.levels[self.levels.keys()[self.current_level]][0]) * 20,\
               len(self.levels[self.levels.keys()[self.current_level]]) * 20
    
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
        level_height = len(level)*20
        level_width = len(level[0])*20
        rect_list += [rect.Rect(0,0,0,level_height),
                      rect.Rect(0,-100,level_width,100),
                      rect.Rect(0,level_height,level_width,100),
                      rect.Rect(level_width,0,100,level_height)]
        
        for line in range(len(level)):
            for char in range(len(level[line])):
                if level[line][char] == self.land:
                    height = 1
                    tmp_char = char
                    temp_line = line
                    while True:
                        try:
                            if level[line][tmp_char] == self.land:
                                level[line][tmp_char] = None
                                height = 1
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
                                break                                
                            else: 
                                break
                        except IndexError:
                            break
                    rect_list.append(rect.Rect(char*20, line*20, 20, height*20))
        return rect_list
    
    def info(self):
        print "%d levels loaded" % len(self.levels)
        
def main():
    a = LevelManager()
    a.load_level("meow")
    #print a.get_level("meow")
    print a.interpret("meow")

if __name__ == "__main__" :
    main()
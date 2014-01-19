import math
import pygame

try:
    import android
    from android import mixer
except:
    print 'ohh, snap!  Android was not imported'
import player
from time import sleep

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 1920 #800
SCREEN_HGHT = 1080 #480
GROUND = SCREEN_HGHT-160
GRAVITY = 0.25 # px/s^2
TERMINAL_VELOCITY = 30

class Core:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HGHT
        #TODO: change this to proper background
        # 1080p 1920*1080
        self.background_base = WHITE 
        self.back = False 
        self.forward = False 
        self.m_left = False
        self.m_right = False
        
    def on_init(self):
        """
        Create the game window
        """
        
        self._running = True
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size) #this is the main display surface

<<<<<<< HEAD
        self.background_image = pygame.image.load('res/background_rocky.png').convert_alpha()
        self.black = pygame.image.load('res/black.png').convert()
        self.level_manager = level_manager.LevelManager()
        self.level_manager.load_level("tut")
        self.current_level = self.level_manager.interpret("tut")
        map = self.level_manager.get_level("tut")
        x,y = 0,0
        for l in map:
            for c in l:
                if c == self.level_manager.land:
                    self._display_surf.blit(self.black,(x,y))
                x+=20
            y+=20
        # Get android set up
        android.init()
        self.sounds = mixer.Sound('res/song.mp3')
        android.map_key(android.KEYCODE_BACK, pygame.K_DELETE)
                
    def on_event(self,event, anie):    
        if event.type == pygame.QUIT:
            self.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            self.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < 150:
                self.m_left = True
            elif event.pos[0] > 650:
                self.m_right = True
            else:
                if (self.is_pull_down()):
                    anie.jumping = True
        elif event.type == pygame.MOUSEBUTTONUP:
            anie.speed = 0


    def is_pull_down(self):
        initial = pygame.mouse.get_pos()  # gets initial pos of finger
        sleep(0.1)            # wait a bit
        second = pygame.mouse.get_pos()   # gets the "last" position of the finger
        delta_y = initial[1]-second[1]
        if delta_y < 0:
            self.anie.jump_height = delta_y * self.anie.jump_strength
            self.anie.jump_speed = min(30, delta_y / 100)
            return True
        else:
            return False
    
    def is_release(self):
            if pygame.mouse.get_pos() == (0,0):
                return True    
            else:
                return False
    
    def movement(self):
        """ Move the entities that need moving
        """
        if self.m_left and self.m_right: # cannot move left and right at the same time.
            pass
        elif self.m_left:
            if self.anie.rect.move(-self.anie.speed,0).collidelist(self.current_level):
                wall = self.current_level[self.anie.rect.move(-self.anie.speed)\
                                          .collidelist(self.current_level)]
                self.anie.rect.move_ip(-math.fabs(wall.x - (self.anie.rect.x - self.anie.speed)),0)
            else:
                self.anie.rect.move_ip(-self.anie.speed,0)
                
        elif self.m_right: 
            if self.anie.rect.move(self.anie.speed,0).collidelist(self.current_level):
                wall = self.current_level[self.anie.rect.move(self.anie.speed)\
                                          .collidelist(self.current_level)]
                self.anie.rect.move_ip(math.fabs(wall.x + (self.anie.rect.x - self.anie.speed)),0) 
            else:
                self.anie.rect.move_ip(self.anie.speed,0)
                
        if self.anie.jumping:
            if self.anie.rect.move(0,self.anie.jump_speed).collidelist(self.current_level):
                wall = self.current_level[self.anie.rect.move(self.anie.speed)\
                                          .collidelist(self.current_level)]
                self.anie.jump_height -= math.fabs(wall.y - (self.anie.rect.y - self.anie.jump_speed))
            self.anie.rect.move_ip(0,self.anie.jump_speed)
        
        if self.anie.rect.move(0,self.anie.down_speed).collidelist(self.current_level):
            wall = self.current_level[self.anie.rect.move(0,self.anie.down_speed)\
                                      .collidelist(self.current_level)]
            self.anie.down_speed += GRAVITY
            self.anie.rect.move_ip(0,math.fabs(self.y - (self.anie.rect.y - self.anie.downspeed)))
            
    def quit(self):
        pygame.quit()#pygame cleans up itself nicely
        raise SystemExit#terminate python
      

    def on_execute(self):
        '''The game loop'''
        if self.on_init() == False:
            self._running = False

        while(self._running):    
            # Dat DJ
            if mixer.get_busy() == False:
                mixer.music.load('res/song.mp3')
                mixer.music.play()   
                
                clock = pygame.time.Clock()
            
                anie = player.Player()
             
                anie.rect.y = GROUND
                anie.rect.x = SCREEN_WIDTH/2
                
                anie.ground = anie.rect.y
    
        while( self._running ):       
            self._display_surf.fill(self.background_base)    
            self._display_surf.blit(self.background_image, (0,0))
            self._display_surf.blit(anie.image, anie.rect)        
            clock.tick(60)
            pygame.display.update()            # update
            # Allows android to pause the game
            if android:
                if android.check_pause():
                    android.wait_for_resume()
    
            for event in pygame.event.get():
                self.on_event(event, anie)
    
        self.quit()
        

def main():
    game = Core()
    game.on_execute()

main()

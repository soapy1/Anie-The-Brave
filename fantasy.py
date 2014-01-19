import math
from time import sleep

import pygame

import level_manager
import player


try:
    import android
    from android import mixer
except:
    android = None
    print 'ohh, snap!  Android was not imported'

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RES = SCREEN_WIDTH, SCREEN_HGHT = 1600, 900
GROUND = SCREEN_HGHT-160
GRAVITY = 0.25 # px/s^2
TERMINAL_VELOCITY = 30

class Core:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HGHT
        self.on_execute()
        
    def on_init(self):
        """
        Create the game window
        """
        self._running = True
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size) #this is the main display surface
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load('res/background_rocky.png').convert()
        self.black = pygame.image.load('res/black.png').convert_alpha()
        self.level_manager = level_manager.LevelManager()
        self.level_manager.load_level("tut")
        self.current_level = self.level_manager.interpret("tut")
        lvl_map = self.level_manager.next_level()
        self.background_base = BLACK 
        self._display_surf.fill(self.background_base)
        self.back = False 
        self.forward = False 
        self.m_left = False
        self.m_right = False
        self.move_zone_left = 150
        self.move_zone_right = SCREEN_WIDTH-150
        
        self.anie = player.Player() # brosefina
        self.anie.rect.y = GROUND
        self.anie.rect.x = SCREEN_WIDTH/2
        self.anie.ground = self.anie.rect.y
        
        x,y = 0,0
        for l in lvl_map:
            x = 0
            for c in l:
                if c != 'x':
                    self._display_surf.blit(self.black,(x,y))
                x += 20
            y += 20
        # Get android set up
        if android:
            android.init()
            self.sounds = mixer.Sound('res/song.mp3')
            android.map_key(android.KEYCODE_BACK, pygame.K_DELETE)
            mixer.music.play()
        
    def on_event(self,event):    
        if event.type == pygame.QUIT:
            self.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            self.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print "mouse button down", event.pos
            if event.pos[0] < self.move_zone_left:
                self.m_left = True
            elif event.pos[0] > self.move_zone_right:
                self.m_right = True
            else:
                if (self.is_pull_down()):
                    self.anie.jumping = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.m_left,self.m_right = False, False


    def is_pull_down(self):
        initial = pygame.mouse.get_pos()  # gets initial pos of finger
        sleep(0.1)            # wait a bit
        second = pygame.mouse.get_pos()   # gets the "last" position of the finger
        delta_y = initial[1]-second[1]
        if delta_y < 0:
            self.anie.jump_height = delta_y * self.anie.jump_strength
            self.anie.jump_accel = min(0.25, delta_y / 1000)
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
            if self.anie.rect.move(-self.anie.speed,0).collidelist(self.current_level) != -1:
                wall = self.current_level[self.anie.rect.move(-self.anie.speed,0)\
                                          .collidelist(self.current_level)]
                self.anie.rect.move_ip(-math.fabs(wall.x - (self.anie.rect.x - self.anie.speed)),0)
                self.m_left = False
            else:
                self.anie.rect.move_ip(-self.anie.speed,0)
                
        elif self.m_right: 
            if self.anie.rect.move(self.anie.speed,0).collidelist(self.current_level) != -1:
                wall = self.current_level[self.anie.rect.move(self.anie.speed,0)\
                                          .collidelist(self.current_level)]
                print wall
                print self.anie.rect
                self.anie.rect.move_ip(math.fabs(wall.x + (self.anie.rect.x - self.anie.speed)),0)
                self.m_right = False
            else:
                self.anie.rect.move_ip(self.anie.speed,0)
                
        if self.anie.jumping:
            self.anie.up_speed = min((self.anie.up_speed + self.anie.jump_accel \
                                      , TERMINAL_VELOCITY))
            if self.anie.rect.move(0,self.anie.up_speed).collidelist(self.current_level) != -1:
                wall = self.current_level[self.anie.rect.move(0,self.anie.up_speed)\
                                          .collidelist(self.current_level)]
                self.anie.jump_height -= math.fabs(wall.y - (self.anie.rect.y - self.anie.up_speed))
            self.anie.rect.move_ip(0,self.anie.up_speed)
        
        if self.anie.rect.move(0,self.anie.down_speed).collidelist(self.current_level) != -1:
            wall = self.current_level[self.anie.rect.move(0,self.anie.down_speed)\
                                      .collidelist(self.current_level)]
            self.anie.down_speed += GRAVITY
            self.anie.rect.move_ip(0,math.fabs(wall.y - (self.anie.rect.y - self.anie.down_speed)))
   
    def render(self):
        self._display_surf.fill(self.background_base)
        self._display_surf.blit(self.anie.image, self.anie.rect)        
        self.clock.tick(60)
        pygame.display.update()
             
    def quit(self):
        pygame.quit()#pygame cleans up itself nicely
        raise SystemExit#terminate python
      

    def on_execute(self):
        '''The game loop'''
        if self.on_init() == False:
            self._running = False

        while(self._running):    
            # Dat DJ
            if android:             # Pause the game when app is not in focus
                if android.check_pause():
                    mixer.music.pause()
                    android.wait_for_resume()
                    mixer.music.unpause()
            #self._display_surf.blit(self.background_image, (0,0))
            for event in pygame.event.get():
                self.on_event(event)
            self.movement()
            self.render()
            
        self.quit()
        
if __name__ == '__main__':
    Core()

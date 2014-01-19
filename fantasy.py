import pygame
import player
from time import sleep

<<<<<<< HEAD
#try:
#    import android
#except:
#    print 'ohh, snap!  Android was not imported'

try:
    import pygame.mixer as mixer
except ImportError:
    pass
#    import android.mixer as mixer
=======
# try:
#     import android
# except:
#     print 'ohh, snap!  Android was not imported'
>>>>>>> 65583b053355f0b8b89faeca8147f10df969aec4

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 800
SCREEN_HGHT = 480

GROUND = SCREEN_HGHT-160
GRAVITY = 5
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
        self.gravity_effect = 0

    def on_init(self):
        """
        Create the game window
        """
        self._running = True
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size) #this is the main display surface
<<<<<<< HEAD
	self.background_image = pygame.image.load('res/background_rocky.png').convert_alpha()

	pygame.mixer.init(44100,-16,300,1024)

	# Get android set up
#	android.init()


    def on_event(self,event, bro):
#	android.map_key(android.KEYCODE_BACK, pygame.K_DELETE)       	

	if event.type == pygame.QUIT:
	    pygame.quit()
	    mixer.music.stop()
	elif event.type == pygame.K_DELETE:
            pygame.quit()
	elif event.type == pygame.MOUSEBUTTONDOWN:
	    if event.pos[0] < 150:
		bro.speed = -player.MAX_SPEED
	    elif event.pos[0] > 650:
		bro.speed = player.MAX_SPEED
	    else:
		if (self.is_pull_down() == True):
		    bro.jump_up = True
	elif event.type == pygame.MOUSEBUTTONUP:
	    bro.speed = 0
=======

        # Get android set up
        android.init()
        self.background_image = pygame.image.load('res/background_rocky.png').convert_alpha()



    def on_event(self,event, bro):
    #android.map_key(android.KEYCODE_BACK, pygame.K_DELETE)           

        if event.type == pygame.QUIT:
            self.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            self.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < 150:
                bro.speed = -player.MAX_SPEED
            elif event.pos[0] > 650:
                bro.speed = player.MAX_SPEED
            else:
                if (self.is_pull_down()):
                    bro.jump_up = True
        elif event.type == pygame.MOUSEBUTTONUP:
            bro.speed = 0
>>>>>>> 65583b053355f0b8b89faeca8147f10df969aec4


    def is_pull_down(self):
        initial = pygame.mouse.get_pos()  # gets initial pos of finger
        sleep(0.1)            # wait half a sec
        second = pygame.mouse.get_pos()   # gets the "last" position of the finger
        chng = initial[1]-second[1]
        if chng<0:
            return True
        else:
            return False
    
        def is_release(self):
            if pygame.mouse.get_pos() == (0,0):
                return True    
            else:
                return False
    
    def quit(self):
        pygame.quit()#pygame cleans up itself nicely
        raise SystemExit#terminate python
      

    def on_execute(self):

        '''The game loop'''
        if self.on_init() == False:
            self._running = False

<<<<<<< HEAD
	clock = pygame.time.Clock()

	bro = player.Player()
 
	bro.rect.y = GROUND
	bro.rect.x = SCREEN_WIDTH/2
	
	bro.ground = bro.rect.y

	while( self._running ):	

	    # Dat DJ
	    if mixer.get_busy() == False:
		mixer.music.load('res/song.mp3')
		mixer.music.play()   
	     
            self._display_surf.fill(self.background_base)	
	    self._display_surf.blit(self.background_image, (0,0))
	    self._display_surf.blit(bro.image, bro.rect)		
	    clock.tick(10)
	    pygame.display.update()			# update
    
	    self.gravity_effect += GRAVITY

	    
	    bro.rect.x += bro.speed

	    if bro.rect.y < GROUND-60:
		bro.rect.y += self.gravity_effect

	    if bro.jump_up == True:
		bro.rect.move_ip(0,-bro.jump_speed)

	    # Allows android to pause the game
#	    if android:
#		if android.check_pause():
#		    android.wait_for_resume()

=======
        clock = pygame.time.Clock()
    
        bro = player.Player()
     
        bro.rect.y = GROUND
        bro.rect.x = SCREEN_WIDTH/2
        
        bro.ground = bro.rect.y
    
        while( self._running ):       
            self._display_surf.fill(self.background_base)    
            self._display_surf.blit(self.background_image, (0,0))
            self._display_surf.blit(bro.image, bro.rect)        
            clock.tick(60)
            pygame.display.update()            # update
            # Allows android to pause the game
            if android:
                if android.check_pause():
                    android.wait_for_resume()
    
>>>>>>> 65583b053355f0b8b89faeca8147f10df969aec4
            for event in pygame.event.get():
                self.on_event(event, bro)
    
        self.quit()
        

def main():
    game = Core()
    game.on_execute()

main()

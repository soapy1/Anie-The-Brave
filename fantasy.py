import pygame
import player
from time import sleep

try:
    import android
except:
    print 'ohh, snap!  Android was not imported'

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
SCREEN_WIDTH = 800
SCREEN_HGHT = 480

GROUND = SCREEN_HGHT-40
GRAVITY = 5
TERMINAL_VELOCITY = 30

class Core:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HGHT
	self.background = BLACK
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
	# Get android set up
	android.init()


    def on_event(self,event, bro):
	android.map_key(android.KEYCODE_BACK, pygame.K_DELETE)       	

	if event.type == pygame.QUIT:
	    pygame.quit()
	elif event.type == pygame.K_DELETE:
            pygame.quit()
	elif event.type == pygame.MOUSEBUTTONDOWN:
	    self.background = GREEN
	    if event.pos[0] < 150:
		bro.speed = -player.MAX_SPEED
	    elif event.pos[0] > 650:
		bro.speed = player.MAX_SPEED
	    else:
		if (self.is_pull_down() == True):
		    bro.jump_up = True
	elif event.type == pygame.MOUSEBUTTONUP:
	    bro.speed = 0


    def is_pull_down(self):
	initial = pygame.mouse.get_pos()  # gets initial pos of finger
	sleep(0.1)		    # wait half a sec
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
    
    def on_cleanup(self):
        pygame.quit()#pygame cleans up itself nicely
        raise SystemExit#terminate python
      

    def on_execute(self):


        '''The game loop'''
        if self.on_init() == False:
            self._running = False

	clock = pygame.time.Clock()

	bro = player.Player() 
	bro.rect.y = GROUND
	bro.rect.x = SCREEN_WIDTH/2
	
	bro.ground = bro.rect.y

	while( self._running ):	   
	     
            self._display_surf.fill(self.background)	# colourful
	    self._display_surf.blit(bro.image, bro.rect)		
	    clock.tick(60)
	    pygame.display.update()			# update
    
	    self.gravity_effect += GRAVITY

	    
	    bro.rect.x += bro.speed

	    if bro.rect.y < GROUND-60:
		bro.rect.y += self.gravity_effect

	    if bro.jump_up == True:
		bro.rect.move_ip(0,-bro.jump_speed)

	    # Allows android to pause the game
	    if android:
		if android.check_pause():
		    android.wait_for_resume()

            for event in pygame.event.get():
                self.on_event(event, bro)

        self.on_cleanup()
        

def main():
    game = Core()
    game.on_execute()


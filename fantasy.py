import pygame
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

class Bro (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('res/henry.png').convert()
        self.rect = self.image.get_rect()

class Core:


    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HGHT
	self.background = BLACK
	self.back = False
	self.forward = False

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
	android.map_key(android.KEYCODE_BACK, pygame.QUIT)       	

	if event.type == pygame.QUIT:
            self._running = False
	elif event.type == pygame.MOUSEBUTTONDOWN:
	    if event.pos[0] < 100:
		self.back = True
		self.forward = False
	    if event.pos[0] > 380:
		self.back = False
		self.forward = True
	elif event.type == pygame.MOUSEBUTTONUP:
	    self.back = False
	    self.forward = False

	if event.type == pygame.MOUSEMOTION:
	    bro.rect.x = event.pos[0]
	    bro.rect.y = event.pos[1]
	    self.background = GREEN
	    pass   
 
    
    def on_cleanup(self):
        pygame.quit()#pygame cleans up itself nicely
        raise SystemExit#terminate python
      

    def create_bro(self):
        bro = Bro()
	return bro


    def on_execute(self):

        '''The game loop'''
        if self.on_init() == False:
            self._running = False

	clock = pygame.time.Clock()
	bro = self.create_bro()
	bro.rect.y = SCREEN_HGHT 
	 
	while( self._running ):	   
	     
            self._display_surf.fill(self.background)	# colourful
	    self._display_surf.blit(bro.image, bro.rect)		# draw sef
	    clock.tick(60)
	    pygame.display.flip()			# update

	    if self.back == True:
		bro.rect.x -= 5
	    if self.forward == True:
		bro.rect.x += 5

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


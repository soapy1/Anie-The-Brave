import pygame
try:
    import android
except:
    print 'ohh, snap!  Android was not imported'

class Core:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 600
    
    def on_init(self):
        """
        Create the game window
        """
        self._running = True
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF) #this is the main display surface
        pygame.mixer.pre_init(44100, -16, 1, 1024) #high buffer will result in sound delay, might be a pygame bug
        
    def on_event(self,event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_cleanup(self):
        pygame.quit()#pygame cleans up itself nicely
        raise SystemExit#terminate python
        
    def on_execute(self):
        '''The game loop'''
        if self.on_init() == False:
            self._running = False
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
        self.on_cleanup()
        
def main():
    game = Core()
    game.on_execute()

main()    
print 'this is a fantasy game'

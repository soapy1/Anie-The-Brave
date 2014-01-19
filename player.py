'''
Class that desribes the main character
She is a Player a.k.a Brosefina a.k.a Annie
'''
import pygame

MAX_SPEED = 5

class Player (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('res/annie.png').convert_alpha()
        self.rect = self.image.get_rect()
	
	# Character attributes
	self.health_pnts = 10	    
	self.max_dmg = 10
	self.min_dmg = 5
	self.visc = 6
	self.speed = 0

	self.ground = 0	

	self.jump_up = False
	self.jump_speed = 15
	self.max_jump = 200


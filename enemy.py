import pygame
from random import randint

class BlobMan(pygame.sprite.Sprite):
    def __init__(self, screen):
	pygame.sprite.Sprite.__init__(self)

	self.main_img_one = pygame.image.load('res/enemy_one.png').convert_alpha()
	self.main_img_two = pygame.image.load('res/enemy_two.png').convert_alpha()
	self.main_img_three = pygame.image.load('res/enemy_three.png').convert_alpha()

	self.attack_img_one = pygame.image.load('res/enemy_one_attack.png').convert_alpha()
	self.attack_img_two = pygame.image.load('res/enemy_one_attack_two.png').convert_alpha()

	self.enemy_main = [self.main_img_one, self.main_img_two, self.main_img_three]
	self.enemy_attack = [self.attack_img_one, self.attack_img_one, self.attack_img_two, self.attack_img_two]
	self.rect = self.main_img_one.get_rect()    

	self.fr = 0
	self.health = 10
	self.attack = 2
	self.discovered = False
	self.is_atk = False
	self.scrn = screen

    def is_alive(self):
	if self.health > 0:
	    return True
	else:
	    return False

    def move_inc(self, x, y):
	self.rect.x += x
	self.rect.y += y
	    

    def move_to(self, x, y):
	self.rect.x = x
	self.rect.y = y
    

    def attack_animation(self):
	# TODO: collision
	self.fr += 1
	cur_frame = self.fr%2	
	self.scrn.blit(self.enemy_attack[cur_frame], self.rect)


    # Returns the damage
    def attack_action(self):
	# animation
	self.fr += 1
	cur_frame = self.fr%2	
	self.scrn.blit(self.enemy_attack[cur_frame], self.rect)

	hit = randint(0,3)
	if (hit == 0):
	    return self.attack
	else:
	    return 0

    
    def move(self, anie_x, anie_y):
	if (self.rect.x < anie_x):
	    self.rect.x += 1
	    self.render()
	elif (self.rect.x > anie_x):
	    self.rect.x -= 1
	    self.render()

	dist = abs(self.rect.x - anie.x)
	if (dist < 10):
	    dmg = self.attack_action()
	    return dmg

	return -1 
	


    def render(self):
	# TODO: collision
	self.fr += 1
	cur_frame = self.fr%3	
	self.scrn.blit(self.enemy_main[cur_frame], self.rect)
	

    def action(self):
	pass

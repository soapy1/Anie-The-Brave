from entities import Entities
import random
import pygame as pg


class Warrior(Entities):
    sprite = pg.sprite.Sprite()
    sprite.image = None #TODO add later
    sprite.rect = sprite.image.get_rect()
    attack_max_frame = 3
    action_max_frame = 3
    def __init__(self, spawn, health, max_dmg , min_dmg):
        super(Warrior,self).__init__(spawn, health, max_dmg , min_dmg)
        self.sprite.move_ip(self.spawn)
        
class Mage(Entities):
    sprite = pg.sprite.Sprite()
    

    

    sprite.image = None #TODO add later
    sprite.rect = sprite.image.get_rect()
    attack_max_frame = 3
    action_max_frame = 3
    discover_max_frame = 3 #will be used iftp
    def __init__(self, spawn, health, max_dmg , min_dmg):
        super(Mage,self).__init__(spawn, health, max_dmg , min_dmg)
        self.sprite.move_ip(self.spawn)
        self.main_img_one = pg.image.load('res/enemy_one.png').convert_alpha()
        self.main_img_two = pg.image.load('res/enemy_two.png').convert_alpha()
        self.main_img_three = pg.image.load('res/enemy_three.png').convert_alpha()
        
    def attack(self):
        #add animation
        self.attacking = True
        return random.randrange(self.min_dmg, self.max_dmg + 1)

    def action(self):
        #add animation
        #teleport ifftp
        return
    
    def idle(self):
        self.idling = True
        #animation, patroling movement
        pass
        
    def on_discover(self):
        self.idle()
        #animation iftp
        pass
        
    def react_attack(self, took_dmg):
        self.health -= took_dmg
        pass #animation
    
    
class Paladin(Entities):
    sprite = pg.sprite.Sprite()
    sprite.image = None #TODO add later
    sprite.rect = sprite.image.get_rect()
    attack_max_frame = 3
    action_max_frame = 3   
    def __init__(self, spawn, health, max_dmg , min_dmg):
        super(Paladin,self).__init__(spawn, health, max_dmg , min_dmg)
        self.sprite.move_ip(self.spawn)
        

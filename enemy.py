import math
import pygame
from random import randint
from pygame.transform import flip

TERMINAL_VELOCITY = 30
GRAVITY = 0.25


class BlobMan(pygame.sprite.Sprite):
    def __init__(self, screen, cur_lvl, spawn_x, spawn_y):
        pygame.sprite.Sprite.__init__(self)

        self.main_img_one = pygame.image.load('res/enemy_one.png').convert_alpha()
        self.main_img_two = pygame.image.load('res/enemy_two.png').convert_alpha()
        self.main_img_three = pygame.image.load('res/enemy_three.png').convert_alpha()

        self.attack_img_one = pygame.image.load('res/enemy_one_attack.png').convert_alpha()
        self.attack_img_two = pygame.image.load('res/enemy_one_attack_two.png').convert_alpha()

        self.enemy_main = [self.main_img_one, self.main_img_two, self.main_img_three]
        self.enemy_attack = [self.attack_img_one, self.attack_img_one, self.attack_img_two, self.attack_img_two]
        self.rect = self.main_img_one.get_rect()

        self.rect.x = spawn_x
        self.rect.y = spawn_y

        self.speed = 8
        self.fr = 0
        self.health = 10
        self.attack = 2
        self.discovered = False
        self.is_atk = False
        self.scrn = screen
        self.down_speed = 0
        self.up_speed = 20
        self.current_lvl = cur_lvl
        # negative is left, positive is right
        self.side = -1

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def _move_inc(self, x, y):
        self.rect.x += x
        self.rect.y += y


    def _move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y


    def _attack_animation(self):
        # TODO: collision
        self.fr += 1
        cur_frame = self.fr % 4
        self.scrn.blit(self.enemy_attack[cur_frame], self.rect)


    # Returns the damage
    def attack_action(self):
        # animation
        self.fr += 1
        cur_frame = self.fr % 4
        if self.side > 0:
            self.scrn.blit(flip(self.enemy_attack[cur_frame], True, False), self.rect)
        else:
            self.scrn.blit(self.enemy_attack[cur_frame], self.rect)

        hit = randint(0, 3)
        if (hit == 0):
            return self.attack
        else:
            return 0


    def movement_collision(self):
        y = self.rect.y
        ds = self.down_speed
        h = self.rect.height
        if self.rect.move(0, ds).collidelist(self.current_lvl) != -1:
            wall = self.current_lvl[self.rect.move(0, ds) \
                .collidelist(self.current_lvl)]
            self.rect.move_ip(0, math.fabs(ds - (y + h + ds - wall.y)))
            self.down_speed = 0
        else:
            self.rect.move_ip(0, self.down_speed)
        self.down_speed = min(TERMINAL_VELOCITY, (self.down_speed + GRAVITY))

        if self.rect.move(0, self.up_speed).collidelist(self.current_lvl) != -1:
            wall = self.current_lvl[self.rect.move(0, self.up_speed).collidelist(self.current_lvl)]
            self.rect.move_ip(0, -self.up_speed)


    def move(self, anie_x, anie_wid):

        self.side = (self.rect.x + self.rect.width) - (anie_x + anie_wid)
        self.movement_collision()
        if (self.rect.x < anie_x):
            self.rect.x += self.speed
            self.render()
        elif (self.rect.x > anie_x):
            self.rect.x -= self.speed
            self.render()

        dist = abs(self.side)
        if (dist < 150):
            dmg = self.attack_action()
            return dmg

        return -1


    def render(self):
        self.fr += 1
        cur_frame = self.fr % 3

        if self.side > 0:
            self.scrn.blit(flip(self.enemy_main[cur_frame], True, False), self.rect)
        else:
            self.scrn.blit(self.enemy_main[cur_frame], self.rect)


    def action(self):
        pass

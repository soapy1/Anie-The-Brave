import math
from time import sleep
import enemy
import pygame

import level_manager
import player

try:
    import android
    from android import mixer
except:
    android = None
    from pygame import mixer

    print 'ohh, snap!  Android was not imported'

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RES = SCREEN_WIDTH, SCREEN_HGHT = 1600, 900
GROUND = SCREEN_HGHT - 160
GRAVITY = 0.25 # px/s^2
TERMINAL_VELOCITY = 30
SCROLL_THRESHOLD = int(0.3 * SCREEN_WIDTH)
text_list = ["Hi Sophia,", "it was great working with you,", "hopefully we will meet again!"]
text_two = ["What up Alan", "I'm sure we will", "/"]


class Core:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.on_execute()

    def on_init(self):
        """
        Create the game window
        """
        self._running = True
        pygame.init()
        try:
            self._display_surf = pygame.display.set_mode(RES, pygame.FULLSCREEN) #this is the main display surface
        except:
            self._display_surf = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.background_image = pygame.image.load('res/background_looping.png').convert()
        self.black = pygame.image.load('res/black.png').convert_alpha()
        self.level_manager = level_manager.LevelManager()
        self.level_manager.load_level("levels/tut")
        self.current_level = self.level_manager.interpret("levels/tut")
        lvl_map = self.level_manager.next_level()
        self.background_base = WHITE
        self._display_surf.fill(self.background_base)
        self.back = False
        self.forward = False
        self.m_left = False
        self.m_right = False
        self.move_zone_left = 150
        self.move_zone_right = SCREEN_WIDTH - 150
        self.jump_target = 0
        self.text_frame_count = 0
        self.text_count = 0
        self.text_surf = pygame.font.Font("School Book New.ttf", 70).render(text_list[0], True, WHITE)
        self.text_surf1 = pygame.font.Font("School Book New.ttf", 70).render(text_list[1], True, WHITE)
        self.text_surf2 = pygame.font.Font("School Book New.ttf", 70).render(text_list[2], True, WHITE)
        self.greet_flo = pygame.font.Font("School Book New.ttf", 50).render(text_two[0], True, GREEN)
        self.greet_bob = pygame.font.Font("School Book New.ttf", 50).render(text_two[1], True, GREEN)
        self.greet_line = pygame.font.Font("School Book New.ttf", 50).render(text_two[2], True, GREEN)

        # Brosefina
        self.sophia = 'here'
        self.anie = player.Player()
        self.anie.rect.y = 50
        self.anie.rect.x = 1000
        self.anie.ground = self.anie.rect.y
        #Camera is a rectangle
        self.camera = pygame.Rect((0, 0), RES)
        self.level_dimensions = self.level_manager.get_current_dimensions()
        self.lvl_surface = pygame.Surface(self.level_manager \
            .get_current_dimensions()).convert_alpha()
        self.bob = enemy.BlobMan(self._display_surf, self.camera, self.current_level, 2000, 0)
        self.flo = enemy.BlobMan(self._display_surf, self.camera, self.current_level, 0, 0)
        self.flo.speed = 12
        #
        #         self.lvl_surface.fill((0,0,0,0))
        #         x,y = 0,0
        #         for l in lvl_map:
        #             x = 0
        #             for c in l:
        #                 if c != 'x':
        #                     self.lvl_surface.fill((0,0,0),pygame.Rect(x,y,20,20))
        #                 x += 20
        #             y += 20
        # Get android set up
        if android:
            android.init()
            self.bg_music = mixer.music.load('res/song.mp3')#the theme just doesn't fit.. Im sorry!
            android.map_key(android.KEYCODE_BACK, pygame.K_DELETE)
            mixer.music.play()

    def on_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE):
            self.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
        #             print "mouse button down", event.pos
            if event.pos[0] < self.move_zone_left:
                self.m_left = True
            elif event.pos[0] > self.move_zone_right:
                self.m_right = True
            else:
                if (self.is_pull_down()):
                    self.anie.jumping = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.anie.jump_frames = int(math.fabs(200 * 1.5))
            self.anie.jumping = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.m_left, self.m_right = False, False


    def is_pull_down(self):
        initial = pygame.mouse.get_pos()  # gets initial pos of finger
        sleep(0.1)            # wait a bit
        second = pygame.mouse.get_pos()   # gets the "last" position of the finger
        delta_y = initial[1] - second[1]
        if delta_y < 0:
            self.anie.jump_frames = int(math.fabs(delta_y * 1.5))
            return True
        else:
            return False

    def is_release(self):
        if pygame.mouse.get_pos() == (0, 0):
            return True
        else:
            return False

    def movement(self):
        """ Move the entities that need moving
        """
        conteract = False
        anie_x = self.anie.rect.x
        anie_y = self.anie.rect.y
        anie_ds = self.anie.down_speed
        anie_height = self.anie.rect.height
        #print "%f y, %f target, %s" % (anie_y, self.jump_target,self.anie.jumping)
        if self.anie.rect.move(0, anie_ds).collidelist(self.current_level) != -1:
            wall = self.current_level[self.anie.rect.move(0, anie_ds) \
                .collidelist(self.current_level)]
            self.anie.rect.move_ip(0, math.fabs((self.anie.rect.y + self.anie.rect.height) - wall.y))
            self.anie.down_speed = 0
            self.anie.jump_frames = 0
        else:
            self.anie.rect.move_ip(0, self.anie.down_speed)
        self.anie.down_speed = min(TERMINAL_VELOCITY, (self.anie.down_speed + GRAVITY))

        if self.anie.jump_frames <= 0:
            self.anie.jumping = False

        if self.m_left and self.m_right: # cannot move left and right at the same time.
            pass

        elif self.m_left:
            if self.anie.rect.move(-self.anie.speed, 0).collidelist(self.current_level) != -1:
                pass
            #                 wall = self.current_level[self.anie.rect.move(-self.anie.speed,0)\
            #                                           .collidelist(self.current_level)]
            #                 self.anie.rect.move_ip(-math.fabs(anie_x-self.anie.speed+wall.x),0)
            #                 print wall.x,(anie_x-self.anie.speed+wall.x)
            else:
                self.anie.rect.move_ip(-self.anie.speed, 0)
                self.pan_camera_l()

        elif self.m_right:
            if self.anie.rect.move(self.anie.speed, 0).collidelist(self.current_level) != -1:
                pass
            #                 wall = self.current_level[self.anie.rect.move(self.anie.speed,0)\
            #                                           .collidelist(self.current_level)]
            #                 self.anie.rect.move_ip(math.fabs(self.anie.speed - \
            #                                     (anie_x + self.anie.speed)-wall.x),0)
            #                 print wall.x,anie_x

            else:
                self.anie.rect.move_ip(self.anie.speed, 0)
                self.pan_camera_r()

        if self.anie.jumping:
            self.anie.jump_frames -= 1
            self.anie.up_speed = min((math.fabs(self.anie.up_speed) + math.fabs(self.anie.jump_accel) \
                                          , TERMINAL_VELOCITY))
            if self.anie.rect.move(0, -self.anie.up_speed).collidelist(self.current_level) != -1:
                wall = self.current_level[self.anie.rect.move(0, -self.anie.up_speed) \
                    .collidelist(self.current_level)]
                self.anie.rect.move_ip(0, -math.fabs(self.anie.rect.y - (wall.y + wall.height)))
                self.anie.jumping = False
                self.anie.down_speed = GRAVITY
            else:
                self.anie.rect.move_ip(0, -self.anie.up_speed)


    def pan_camera_r(self):
        """ Pan the camera right.
        """
        #when its time to scroll
        if self.anie.rect.x - self.camera.x > SCREEN_WIDTH - SCROLL_THRESHOLD:
            if self.sophia == 'here':
                self.sophia = 'Sophia'
                # when edge is reached
            if self.camera.x + self.anie.speed + SCREEN_WIDTH > self.level_dimensions[0]:
                self.camera.move_ip(self.level_dimensions[0] - self.camera.x - SCREEN_WIDTH, 0)
            else:
                self.camera.move_ip(self.anie.speed, 0)

    def pan_camera_l(self):
        """ Pan the camera left.
        """
        #when its time to scroll
        if self.anie.rect.x - self.camera.x < SCROLL_THRESHOLD:
            # when edge is reached
            if self.camera.x - self.anie.speed < 0:
                self.camera.move_ip(-self.camera.x, 0)
            else:
                self.camera.move_ip(-self.anie.speed, 0)

    def render(self):
        self._display_surf.blit(self.background_image, (0, 0), self.camera)
        for e in self.current_level:
            #orange
            self._display_surf.fill((255, 165, 0), e.move(-self.camera.x, 0))

        #self._display_surf.blit(self.lvl_surface,(0,0),self.camera)
        if self.sophia == 'Sophia':
            if self.text_frame_count == 100 or \
                            self.text_frame_count == 200:
                self.text_count += 1
            self.text_frame_count += 1;
            if self.text_count == 0:
                self._display_surf.blit(self.text_surf, (100, 100))
            if self.text_count == 1:
                self._display_surf.blit(self.text_surf, (100, 100))
                self._display_surf.blit(self.text_surf1, (100, 200))
            if self.text_count == 2:
                self._display_surf.blit(self.text_surf, (100, 100))
                self._display_surf.blit(self.text_surf1, (100, 200))
                self._display_surf.blit(self.text_surf2, (100, 300))

        self._display_surf.blit(self.anie.image, self.anie.rect.move(-self.camera.x, 0))

        self._display_surf.blit(self.greet_flo, (self.flo.rect.x + 50, 50))
        self._display_surf.blit(self.greet_bob, (self.bob.rect.x + 50, 150))
        self._display_surf.blit(self.greet_line, (self.flo.rect.x + 50, 100))
        self._display_surf.blit(self.greet_line, (self.bob.rect.x + 50, 200))
        self.flo.move(self.anie.rect.x, self.anie.rect.width / 2)
        self.bob.move(self.anie.rect.x, self.anie.rect.width / 2)
        self._display_surf.blit(self.flo.enemy_main[self.flo.fr % 3],
                                self.flo.rect.move(-self.camera.x,0))
        self._display_surf.blit(self.bob.enemy_main[self.bob.fr % 3],
                                self.bob.rect.move(-self.camera.x, 0))
        self.clock.tick(self.fps)
        pygame.display.update()

    def quit(self):
        pygame.quit()  # pygame cleans up itself nicely
        raise SystemExit  # terminate python


    def on_execute(self):
        '''The game loop'''
        if self.on_init() == False:
            self._running = False

        while (self._running):
            # Dat DJ
            if android:             # Pause the game when app is not in focus
                if android.check_pause():
                    mixer.pause()
                    android.wait_for_resume()
                    mixer.unpause()

            for event in pygame.event.get():
                self.on_event(event)
            self.movement()
            #             if android:
            #                 if not mixer.music_channel.get_busy():
            #                     mixer.music.play()
            self.render()

        self.quit()


if __name__ == '__main__':
    Core()

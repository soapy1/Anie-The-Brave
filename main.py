import pygame

import fantasy


try:
    import android
    from android import mixer
except:
    android = None
    print 'ohh, snap!  Android was not imported'
        
SCREEN_WIDTH = 800
SCREEN_HGHT = 480
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

def is_clicked(btn_x, btn_y, mou_x, mou_y, btn_w, btn_h):
    if (mou_x > btn_x) and (mou_x < btn_x+btn_w) and (mou_y > btn_y) and (mou_y < btn_y+btn_h):
        return True
    else:    
        return False

def main():
    running = True
    pygame.init()
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_DELETE)
    size = width, height = SCREEN_WIDTH, SCREEN_HGHT
    background = WHITE 
    scr = pygame.display.set_mode(size)

    background_image = pygame.image.load('res/background_main_menu.png').convert()
 
    new_game_img=('res/new_game_btn.png')
    quit_img=('res/quit_btn.png')

    new_game_btn = pygame.image.load(new_game_img).convert_alpha()
    quit_btn = pygame.image.load(quit_img).convert_alpha()
    ngb_pos = (200, 200)
    qb_pos = (200, 340)

    btn_width = new_game_btn.get_size()[0]    # Buttons are the same size
    btn_height = new_game_btn.get_size()[1]

    clock = pygame.time.Clock()

    while running == True:

    # Allows android to pause the game
        if android:
            if android.check_pause():
                android.wait_for_resume()

        clock.tick(60)
        scr.blit(background_image, (0,0))
        scr.blit(new_game_btn, ngb_pos)
        scr.blit(quit_btn, qb_pos) 
        pygame.display.flip()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_clicked(ngb_pos[0], ngb_pos[1], event.pos[0], event.pos[1], btn_width, btn_height):
                    game = fantasy.Core()
                if is_clicked(qb_pos[0], qb_pos[1], event.pos[0], event.pos[1], btn_width, btn_height):
                    running = False
main()

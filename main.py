import fantasy
import pygame
        
SCREEN_WIDTH = 800
SCREEN_HGHT = 480
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

def is_clicked(btn_x, btn_y, mou_x, mou_y):
    if (mou_x > btn_x) and (mou_x < btn_x+200) and (mou_y > btn_y) and (mou_y < btn_y+100):
	return True
    else:	
	return False

def main():
    #game = fantasy.Core()
    #game.on_execute()
    running = True
    pygame.init()
    size = width, height = SCREEN_WIDTH, SCREEN_HGHT
    background_base = WHITE 
    scr = pygame.display.set_mode(size)

    new_game_btn = pygame.image.load('res/new_game_btn.png').convert()
    quit_btn = pygame.image.load('res/quit_btn.png').convert()
    ngb_pos = (200, 200)
    qb_pos = (200, 340)

    clock = pygame.time.Clock()

    while running == True:
	clock.tick(60)
	scr.fill(WHITE)
	scr.blit(new_game_btn, ngb_pos)
	scr.blit(quit_btn, qb_pos) 
	pygame.display.flip()

	for event in pygame.event.get(): 
	    if event.type == pygame.QUIT:
		running = False
	    elif event.type == pygame.KEYDOWN:
		if event.type == pygame.K_ESCAPE:
		    running = False
	    elif event.type == pygame.MOUSEBUTTONDOWN:
		m = pygame.mouse.get_pos()
		if is_clicked(ngb_pos[0], ngb_pos[1], m[0], m[1]):
		    game = fantasy.Core()
		    game.on_execute()
		if is_clicked(qb_pos[0], qb_pos[1], m[0], m[1]):
		    running = False


main()

import pygame
import enemy

def main():
    pygame.init()
    scrn = pygame.display.set_mode([500,500])
    game = True
    
    mon = enemy.BlobMan(scrn, 0, 0)
    clock = pygame.time.Clock()

    while game == True:
	clock.tick(60)
	scrn.fill((0,0,0))

        pos =  0
        mon.move(pos)
        print pos
#        mon.attack_animation()

	pygame.display.flip()

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		pygame.quit()
            elif event.type == pygame.KEYDOWN: 
		if event.key == pygame.K_q:
		    pygame.quit()
		elif event.key == pygame.K_w:
		    pos += 10
		elif event.key == pygame.K_s:
		    pos -= 10
		elif event.key == pygame.K_p:
		    mon.is_atk == True
		elif event.key == pygame.K_l:
		    mon.is_atk == False
		


main()

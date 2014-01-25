import pygame
import enemy

def main():
    pygame.init()
    scrn = pygame.display.set_mode([500,500])
    game = True
    
    mon = enemy.BlobMan()
    clock = pygame.time.Clock()

    while game == True:
	clock.tick(60)
	scrn.fill((0,0,0))
	mon.is_atk = True

	if mon.is_atk == True:
	    mon.attack_animation(scrn)
	else:
	    mon.render(scrn)

	pygame.display.flip()

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		self.quit()
            elif event.type == pygame.KEYDOWN: 
		if event.key == pygame.K_q:
		    pygame.quit()
		elif event.key == pygame.K_w:
		    mon.move_inc(0,1)
		elif event.key == pygame.K_s:
		    mon.move_inc(0,-1)
		elif event.key == pygame.K_p:
		    mon.is_atk == True
		elif event.key == pygame.K_l:
		    mon.is_atk == False
		


main()

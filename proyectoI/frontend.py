import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1080,720))
pygame.display.set_caption("CFS")


font = pygame.font.SysFont('Arial', 15)

		

while True:

	posx = 20
	posy = 20
	tmp = pygame.draw.rect(window, (154, 180, 200), (10,10,100,120))
	cpu_name = window.blit(font.render('cpu' + str(1), True, (255,0,0)), tmp.topleft)
	px = tmp.centerx - 5
	py = tmp.centery - 10
	process = window.blit(font.render('p' + str(1), True, (255,0,0)), (px, py))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
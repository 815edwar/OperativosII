import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1080,720))
pygame.display.set_caption("CFS")


queue = pygame.draw.rect(window, (154, 180, 200), (10,10,300,100))
tmp = pygame.draw.circle(window,(80,70,120), (200,150), 20)
font = pygame.font.SysFont('Arial', 15)
px = tmp.centerx-6
py = tmp.centery-10
process = window.blit(font.render('p50', True, (255,0,0)), (px,py))
window.blit(process, queue)

		

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
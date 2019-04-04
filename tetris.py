import math
import random
import pygame
import os

os.environ['SDL_AUDIODRIVER'] = 'dummy'


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

screenHeight = 500
screenWidth = 250
outline = 1
grid = 25

pygame.init()
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("TETRIS")

running = True
hasPiece = False
gameOver = False

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

pieceX = 0
pieceY = 0
spd = 10
moveSpeed = 25

nPieces = 0
currentPieces = []
currentFloor = [screenHeight] * 10

def block(start):
	global hasPiece
	global pieceY
	global pieceX
	global currentFloor
	global currentPieces
	global nPieces
	global gameOver

	if not hasPiece:
		hasPiece = True
		pieceY = 100
		pieceX = start


	if hasPiece:
		if (key[pygame.K_DOWN]):
			pieceY += 3*spd
		else:
			pieceY += spd
		currentLocation = int(pieceX/25) 

		if (pieceY >= currentFloor[currentLocation] - grid or key[pygame.K_SPACE]):
			pieceY = currentFloor[currentLocation] - grid
			currentFloor[currentLocation] -= grid
			hasPiece = False
			nPieces += 1
			if pieceY == 150:
				gameOver = True
				pygame.time.delay(500)
				return
			currentPieces.append([pieceX, pieceY])
			clear = True

			for floor in currentFloor:
				if floor == screenHeight:
					clear = False
					break

			if (clear):
				for n in range(10):
					currentFloor[n] += grid
				for blocks in currentPieces:
					blocks[1] += grid
				pygame.draw.rect(window, white, (0, screenHeight - grid,screenWidth,grid))
				pygame.display.update()
				pygame.time.delay(50)

		if key[pygame.K_RIGHT] and currentLocation < 9 and pieceY < currentFloor[currentLocation + 1]:
			if (pieceX + moveSpeed + grid) > screenWidth:
				pieceX = screenWidth - grid
			else:
				pieceX += moveSpeed

		if key[pygame.K_LEFT] and currentLocation > 0 and  pieceY < currentFloor[currentLocation - 1]:
			if (pieceX - moveSpeed) < 0:
				pieceX = 0
			else:
				pieceX -= moveSpeed

		if key[pygame.K_r]:
			nPieces = 0
			currentPieces = []
			currentFloor = [screenHeight] * 10
			hasPiece = False
			pieceY = 0
	return 



#MAIN LOOP

while(running):
	key = pygame.key.get_pressed()
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			running = False
			break
	if key[pygame.K_q]:
		running = False
		break

	block((random.randint(0, (screenWidth - grid)/grid))*grid)
	while(gameOver):
		for event in pygame.event.get():
			if (event.type == pygame.QUIT or key[pygame.K_q]):
				running = False
				gameOver = False
				pygame.quit()
				exit()
		if key[pygame.K_r]:
			gameOver = False
			nPieces = 0
			currentPieces = []
			currentFloor = [screenHeight] * 10
			hasPiece = False
			pieceY = 0

		key = pygame.key.get_pressed()
		window.blit(pygame.image.load('gameover.png'),(0,0))
		pygame.display.update()
	window.fill(black)
	pygame.draw.rect(window, red, (0,150, 250, 350))

	pygame.draw.rect(window, blue, (pieceX,pieceY,grid,grid))
	pygame.draw.rect(window, black, (pieceX,pieceY,grid,grid), outline)
	myfont = pygame.font.SysFont('Comic Sans MS', 25)
	t1 = myfont.render('Arrow keys to move', False, white)
	t2 = myfont.render('R to restart', False, white)
	t3 = myfont.render('Q to quit', False, white)
	t4 = myfont.render('Space to instant drop', False, white)



	window.blit(t1,(0,5))
	window.blit(t2,(0,40))
	window.blit(t3,(0,75))
	window.blit(t4,(0,110))

	for p in currentPieces:
		if (p != None):
			pygame.draw.rect(window, green, (p[0], p[1], grid, grid))
			pygame.draw.rect(window, black, (p[0], p[1], grid, grid), outline)

	pygame.display.update()
	if not hasPiece:
		pieceY = 0
	pygame.time.delay(50)

pygame.quit()
exit()


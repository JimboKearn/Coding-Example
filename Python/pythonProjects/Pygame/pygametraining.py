import pygame
import time
import random


#Initialize pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

block_size = 10
FPS = 15

font = pygame.font.SysFont("impact", 25)

def message_to_screen(msg, color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, (display_width/2 - 200, display_height/2))


# Game loop
def gameLoop():
	gameExit = False
	gameOver = False

	lead_x = display_width/2
	lead_y = display_height/2

	lead_x_change = 0
	lead_y_change = 0

	randAppleX = random.randrange(0, display_width - block_size)
	randAppleY = random.randrange(0, display_height - block_size)

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(white)
			message_to_screen("GAME OVER, Press SPACE to play again or Q to quit", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_SPACE:
						gameLoop()

		for event in pygame.event.get():
	 		if event.type == pygame.QUIT:
	 			gameExit = True
	 		if event.type == pygame.KEYDOWN:
	 			if event.key == pygame.K_RIGHT:
	 				lead_y_change = 0
	 				lead_x_change = block_size
	 			elif event.key == pygame.K_LEFT:
	 				lead_y_change = 0
	 				lead_x_change = -block_size
	 			elif event.key == pygame.K_UP:
	 				lead_x_change = 0
	 				lead_y_change = -block_size
	 			elif event.key == pygame.K_DOWN:
	 				lead_x_change = 0
	 				lead_y_change = block_size

		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
			gameOver = True

		lead_x += lead_x_change
		lead_y += lead_y_change
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, red, (randAppleX, randAppleY, block_size, block_size))
		pygame.draw.rect(gameDisplay, black, (lead_x, lead_y, block_size, block_size))
		pygame.display.update()

		clock.tick(FPS)



	pygame.quit()
	quit()

gameLoop()
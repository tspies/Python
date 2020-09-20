import pygame as pg

#pylint: disable=no-member
pg.init()
#pylint: disable=no-member

#Screen Set-up
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Space Invaders")
icon = pg.image.load("my-icons-collection/png/ufo_basic.png")
pg.display.set_icon(icon)

#Background
background = pg.image.load("my-icons-collection/png/background.gif")

#Player
player = pg.image.load("my-icons-collection/png/spaceship_epic.png")
playerImg = pg.transform.scale(player, (50, 50))
playerX = 388
playerY = 480
playerPos = [388, 480]
playerXMoveSpeed = 0
playerYMoveSpeed = 0

def drawBackground():
	screen.blit(background, (0, 0))

def drawPlayer(playerPos):
	screen.blit(playerImg, playerPos)

def boundryCheck(playerPos):
	if (playerPos[0] > 765):
		playerPos[0] = 765
	elif (playerPos[0] < 4):
		playerPos[0] = 4
	if (playerPos[1] > 565):
		playerPos[1] = 565
	elif (playerPos[1] < 4):
		playerPos[1] = 4
	return playerPos

#Game Loop
run = True
while run:
	screen.fill(((0, 0, 0)))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT:
					playerXMoveSpeed = 5
			if event.key == pg.K_LEFT:
				playerXMoveSpeed = -5
			if event.key == pg.K_UP:
				playerYMoveSpeed = -4.5
			if event.key == pg.K_DOWN:
				playerYMoveSpeed = 4.5
		if event.type == pg.KEYUP:
			if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
				playerXMoveSpeed = 0
			if event.key == pg.K_UP or event.key == pg.K_DOWN:
				playerYMoveSpeed = 0
	playerPos[0] += playerXMoveSpeed
	playerPos[1] += playerYMoveSpeed
	playerPos = boundryCheck(playerPos)
	drawBackground()
	drawPlayer(playerPos)
	pg.display.update()
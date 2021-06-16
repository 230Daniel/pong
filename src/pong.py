import pygame as pg
from Game.player import Player
from Game.ball import Ball

WIDTH = 600
HEIGHT = 400
FPS = 60

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
clock = pg.time.Clock()

ballImage = pg.image.load("Game/ball.png").convert_alpha()
ballImage = pg.transform.smoothscale(ballImage, (80, 80))

player = Player(WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT, ballImage)

all_sprites = pg.sprite.Group()
all_sprites.add(player)

running = True

while running:

	clock.tick(FPS)
	for event in pg.event.get():

		if event.type == pg.QUIT:
			running = False

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_RETURN:
				all_sprites = pg.sprite.Group()
				player = Player(WIDTH, HEIGHT)
				all_sprites.add(player)
				ball = Ball(WIDTH, HEIGHT, ballImage)
				all_sprites.add(ball)

	if ball.game_over:
		screen.fill((255, 0, 0))
	else:
		pressed_keys = pg.key.get_pressed()
		player.update(pressed_keys)
		ball.update()

		if pg.sprite.collide_rect(player, ball):
			ball.collidedWithPaddle()

		screen.fill((0, 0, 0))

		for sprite in all_sprites:
			screen.blit(sprite.surf, sprite.rect)
		screen.blit(ball.image, ball.rect)

	pg.display.flip()       

pg.quit()
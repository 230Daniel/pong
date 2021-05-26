import pygame as pg
import random

class Ball(pg.sprite.Sprite):
	def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		super(Ball, self).__init__()
		self.SCREEN_WIDTH = SCREEN_WIDTH
		self.SCREEN_HEIGHT = SCREEN_HEIGHT
		self.surf = pg.Surface((25, 25))
		pg.draw.circle(self.surf, (255, 255, 255), (25/2, 25/2), 25/2)
		self.rect = self.surf.get_rect(
			center=(
				50,
				SCREEN_HEIGHT / 2
            )
		)
		self.SPEED = 10
		self.directionX = self.SPEED
		self.directionY = random.randint(-5, 5)
		self.game_over = False

	def update(self):
		self.rect.move_ip(self.directionX, self.directionY)
		if(self.rect.left <= 0):
			self.directionX = self.SPEED
		if(self.rect.right > self.SCREEN_WIDTH):
			self.game_over = True
		if(self.rect.top <= 0 or self.rect.bottom >= self.SCREEN_HEIGHT):
			self.directionY *= -1

	def collidedWithPadel(self):
		if(self.directionX > 0):
			self.directionX *= -1
			self.directionY = random.randint(-5, 5)
			self.update()

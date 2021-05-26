import pygame as pg

class Player(pg.sprite.Sprite):
	def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		super(Player, self).__init__()
		self.SCREEN_WIDTH = SCREEN_WIDTH
		self.SCREEN_HEIGHT = SCREEN_HEIGHT
		self.surf = pg.Surface((25, 75))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(
			center=(
				SCREEN_WIDTH - 50,
				SCREEN_HEIGHT / 2
            )
		)

	def update(self, pressed_keys):
		if(pressed_keys[pg.K_w] or pressed_keys[pg.K_UP]):
			self.rect.move_ip(0, -5)
		if(pressed_keys[pg.K_s] or pressed_keys[pg.K_DOWN]):
			self.rect.move_ip(0, 5)

		if(self.rect.top < 0):
			self.rect.top = 0
		if(self.rect.bottom > self.SCREEN_HEIGHT):
			self.rect.bottom = self.SCREEN_HEIGHT

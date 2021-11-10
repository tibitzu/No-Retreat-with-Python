class Entity:
	def __init__(self, x, y, sprite, name):
		self.x = x
		self.y = y
		self.sprite = sprite
		self.name = name
		self.blocks_movement = True

	def move(self, dx, dy):
		self.x = dx
		self.y = dy

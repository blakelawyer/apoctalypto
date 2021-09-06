import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.HP = 100 # make this based on CON and level later

        self.strength = 5 # make this a default attribute value later, 5 is arbitrary
        self.agility = 5
        self.constitution = 5
        self.luck = 5

        self.experience = 0
        self.level = 1

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.HP = 100 # make this based on CON and level later

        self.strength = 5 # make this a default attribute value later, 5 is arbitrary
        self.agility = 5
        self.constitution = 5
        self.luck = 5

        self.experience = 0
        self.level = 1

        self.level = 1

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls_or_player(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls_or_player(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
            if self.player.x == self.x + dx and self.player.y == self.y + dy: #not sure if this works pls test someone
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
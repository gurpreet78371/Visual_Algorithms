import pygame
from pygame.locals import *
import random
import math
maroon = (130, 0, 0)
class button():
	def __init__(self,color,x,y,width,height,font_size, text= ""):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.font_size = font_size
		self.text = text

	def draw(self,win,outline = None):
		if outline != None:
			pygame.draw.rect(win,outline,(self.x-2,self.y-2,self.width+4,self.height+4),2)
		pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),-1)

		if self.text != "":
			font = pygame.font.SysFont('comicsans',self.font_size)
			text = font.render(self.text,1,self.color)
			win.blit(text,(self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))

	def isOver(self,pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False

	def change(self,color):
		self.color = color

class node():
    def __init__(self, color, num, x, y, radius, text = ""):
        self.color = color
        self.num = num
        self.x = x
        self.y = y
        self.radius = radius
        self.text = text

    def draw(self, screen,color=maroon):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)
        if self.text != "":
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(str(self.num), 1, maroon)
            screen.blit(text, ((self.x - text.get_width() / 2), self.y - text.get_height() / 2))

    def change_color(self, change_color):
        self.color = change_color

    def isOver(self, pos):
        if ((self.x)-pos[0])**2 + ((self.y)-pos[1])**2 - (self.radius**2) <=0:
                return True
        return False


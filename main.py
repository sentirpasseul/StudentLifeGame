import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

student = pygame.image.load('src/sprites/characters/main_character/main_character.png')
student_active = pygame.image.load('src/sprites/characters/main_character/main_character_active.png')